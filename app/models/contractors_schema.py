# models/contractors_model.py
from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import date


class Contractor(SQLModel, table=True):
    __tablename__ = "contractors"

    contractor_id: UUID = Field(default_factory=uuid4, primary_key=True, foreign_key="users.user_id")
    registration_number: str = Field(nullable=False, unique=True, max_length=50)
    registration_date: date = Field(nullable=False)
    contract_file: Optional[str] = Field(default=None, unique=True, max_length=50)
    sign_date: Optional[str] = Field(default=None, max_length=50)
    service: str = Field(nullable=False, max_length=255)
    service_price: int = Field(nullable=False)
    website: Optional[str] = Field(default=None, max_length=255)
    intervention: str = Field(nullable=False, max_length=50)
    admin_id: Optional[UUID] = Field(default=None, foreign_key="administrators.admin_id")