from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy import DateTime, ForeignKey, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.session import Base

def new_id() -> str: return str(uuid4())
def utcnow() -> datetime: return datetime.now(timezone.utc)
class Workspace(Base):
    __tablename__ = "workspaces"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    name: Mapped[str] = mapped_column(String(160), nullable=False)
    workspace_type: Mapped[str] = mapped_column(String(24), default="internal", nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, nullable=False)
    campaigns: Mapped[list["Campaign"]] = relationship(back_populates="workspace", cascade="all, delete-orphan")
class Campaign(Base):
    __tablename__ = "campaigns"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    workspace_id: Mapped[str] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), index=True)
    name: Mapped[str] = mapped_column(String(180), nullable=False)
    objective: Mapped[str] = mapped_column(String(40), nullable=False)
    status: Mapped[str] = mapped_column(String(24), default="draft", nullable=False)
    channels: Mapped[list] = mapped_column(JSON, default=list, nullable=False)
    brief: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, nullable=False)
    workspace: Mapped[Workspace] = relationship(back_populates="campaigns")
class AgentRun(Base):
    __tablename__ = "agent_runs"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    workspace_id: Mapped[str] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), index=True)
    campaign_id: Mapped[str | None] = mapped_column(ForeignKey("campaigns.id", ondelete="SET NULL"), nullable=True)
    agent_name: Mapped[str] = mapped_column(String(80), nullable=False)
    status: Mapped[str] = mapped_column(String(24), default="queued", nullable=False)
    input_data: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
    output_data: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, nullable=False)
class Approval(Base):
    __tablename__ = "approvals"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    workspace_id: Mapped[str] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), index=True)
    campaign_id: Mapped[str] = mapped_column(ForeignKey("campaigns.id", ondelete="CASCADE"), index=True)
    asset_type: Mapped[str] = mapped_column(String(40), nullable=False)
    asset_id: Mapped[str] = mapped_column(String(36), nullable=False)
    status: Mapped[str] = mapped_column(String(24), default="pending", nullable=False)
    reviewer_note: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, nullable=False)
