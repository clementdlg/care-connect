# models/tickets_model.py
from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime


class Ticket(SQLModel, table=True):
    __tablename__ = "tickets"

    ticket_id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str = Field(nullable=False, max_length=255)
    text: str = Field(nullable=False)
    open_date: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    close_date: Optional[datetime] = Field(default=None)
    user_id: UUID = Field(nullable=False, foreign_key="users.user_id")
    admin_id: Optional[UUID] = Field(default=None, foreign_key="administrators.admin_id")