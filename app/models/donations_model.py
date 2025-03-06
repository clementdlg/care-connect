# models/donations_model.py
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional


class Donation(SQLModel, table=True):
    __tablename__ = "donations"

    collaborator_id: UUID = Field(
        primary_key=True,
        foreign_key="collaborators.collaborator_id"
    )
    ngo_id: UUID = Field(
        primary_key=True,
        foreign_key="ngo.ngo_id"
    )
    bill_file: str = Field(
        nullable=False,
        unique=True,
        max_length=255
    )
    creation_date: datetime = Field(
        nullable=False,
        default_factory=datetime.utcnow
    )
    amount: int = Field(nullable=False)