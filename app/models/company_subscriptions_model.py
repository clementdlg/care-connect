# models/company_subscriptions_model.py
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from typing import Optional


class CompanySubscription(SQLModel, table=True):
    __tablename__ = "company_subscriptions"

    company_id: UUID = Field(primary_key=True, foreign_key="companies.company_id")
    company_subscription_id: UUID = Field(default_factory=uuid4, primary_key=True)
    bonus_consultation_number: int = Field(nullable=False)
    billing_plan: str = Field(nullable=False, max_length=10)
    status: Optional[str] = Field(default=None, max_length=50)
    pack_id: UUID = Field(nullable=False, foreign_key="packs.pack_id")