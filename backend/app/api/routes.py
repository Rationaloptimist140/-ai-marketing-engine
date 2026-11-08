from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.agents.registry import AGENTS
from app.db.session import get_db
from app.models import AgentRun, Campaign, Workspace
from app.schemas.campaign import CampaignCreate, CampaignRead, WorkspaceCreate, WorkspaceRead
router = APIRouter()
@router.get("/health")
def health(): return {"status": "ok", "service": "ai-marketing-engine-api"}
@router.get("/agents")
def list_agents(): return [{"name": a.name, "purpose": a.purpose} for a in AGENTS.values()]
@router.post("/workspaces", response_model=WorkspaceRead, status_code=201)
def create_workspace(payload: WorkspaceCreate, db: Session = Depends(get_db)):
    workspace = Workspace(name=payload.name, workspace_type=payload.workspace_type); db.add(workspace); db.commit(); db.refresh(workspace); return workspace
@router.get("/workspaces", response_model=list[WorkspaceRead])
def list_workspaces(db: Session = Depends(get_db)):
    return list(db.scalars(select(Workspace).order_by(Workspace.created_at.desc())).all())
@router.post("/workspaces/{workspace_id}/campaigns", response_model=CampaignRead, status_code=201)
def create_campaign(workspace_id: str, payload: CampaignCreate, db: Session = Depends(get_db)):
    if db.get(Workspace, workspace_id) is None: raise HTTPException(status_code=404, detail="Workspace not found")
    campaign = Campaign(workspace_id=workspace_id, **payload.model_dump()); db.add(campaign); db.commit(); db.refresh(campaign); return campaign
@router.get("/workspaces/{workspace_id}/campaigns", response_model=list[CampaignRead])
def list_campaigns(workspace_id: str, db: Session = Depends(get_db)):
    if db.get(Workspace, workspace_id) is None: raise HTTPException(status_code=404, detail="Workspace not found")
    return list(db.scalars(select(Campaign).where(Campaign.workspace_id == workspace_id).order_by(Campaign.created_at.desc())).all())
@router.post("/workspaces/{workspace_id}/campaigns/{campaign_id}/agent-runs", status_code=202)
def queue_agent_run(workspace_id: str, campaign_id: str, agent_name: str, db: Session = Depends(get_db)):
    if agent_name not in AGENTS: raise HTTPException(status_code=404, detail="Unknown agent")
    campaign = db.get(Campaign, campaign_id)
    if campaign is None or campaign.workspace_id != workspace_id: raise HTTPException(status_code=404, detail="Campaign not found in workspace")
    run = AgentRun(workspace_id=workspace_id, campaign_id=campaign_id, agent_name=agent_name, status="queued", input_data={"campaign_id": campaign_id})
    db.add(run); db.commit(); db.refresh(run)
    return {"id": run.id, "agent_name": run.agent_name, "status": run.status, "message": "Run queued. Background execution is not enabled in this MVP foundation."}
