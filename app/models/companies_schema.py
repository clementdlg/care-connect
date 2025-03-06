# models/companies_model.py
from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import date


class Company(SQLModel, table=True):
    __tablename__ = "companies"

    company_id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        foreign_key="users.user_id"
    )
    name: str = Field(nullable=False, unique=True, max_length=255)
    website: Optional[str] = Field(default=None, unique=True, max_length=255)
    registration_number: str = Field(nullable=False, unique=True, max_length=50)
    registration_date: date = Field(nullable=False)
    industry: str = Field(nullable=False, max_length=50)
    revenue: int = Field(nullable=False)
    size: int = Field(nullable=False)
    admin_id: Optional[UUID] = Field(default=None, foreign_key="administrators.admin_id")