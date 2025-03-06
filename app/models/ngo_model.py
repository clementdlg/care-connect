# models/ngo_model.py
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional


class Ngo(SQLModel, table=True):
    __tablename__ = "ngo"

    ngo_id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(nullable=False, unique=True, max_length=255)
    registration_number: str = Field(nullable=False, unique=True, max_length=50)
    registration_date: datetime = Field(nullable=False)
    address: str = Field(nullable=False, max_length=255)
    country: str = Field(nullable=False, max_length=50)
    type: str = Field(nullable=False, max_length=255)
    presentation: str = Field(nullable=False)
    website: str = Field(nullable=False, max_length=255)
    phone: str = Field(nullable=False, max_length=50)
    stripe_id: Optional[str] = Field(default=None, unique=True, max_length=50)
    admin_id: Optional[UUID] = Field(default=None, foreign_key="administrators.admin_id")