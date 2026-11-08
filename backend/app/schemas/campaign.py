from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field
class WorkspaceCreate(BaseModel):
    name: str = Field(min_length=2, max_length=160)
    workspace_type: Literal["internal", "client"] = "internal"
class WorkspaceRead(BaseModel):
    id: str
    name: str
    workspace_type: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
class CampaignCreate(BaseModel):
    name: str = Field(min_length=2, max_length=180)
    objective: Literal["affiliate", "agency", "saas_growth"]
    channels: list[str] = Field(default_factory=list, max_length=12)
    brief: str | None = None
class CampaignRead(BaseModel):
    id: str
    workspace_id: str
    name: str
    objective: str
    status: str
    channels: list[str]
    brief: str | None
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
