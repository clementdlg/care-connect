# models/appointments_model.py
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional


class Appointment(SQLModel, table=True):
    __tablename__ = "appointments"

    appointment_id: UUID = Field(default_factory=uuid4, primary_key=True)
    contractor_id: Optional[UUID] = Field(default=None, foreign_key="contractors.contractor_id")
    collaborator_id: Optional[UUID] = Field(default=None, foreign_key="collaborators.collaborator_id")
    appointment_date: datetime = Field(nullable=False)
    creation_date: datetime = Field(nullable=False, default_factory=datetime.utcnow)
    status: Optional[str] = Field(default=None, max_length=50)
    bill_file: str = Field(nullable=False, unique=True, max_length=255)
    place: str = Field(nullable=False, max_length=6)
    note: Optional[int] = Field(default=None)