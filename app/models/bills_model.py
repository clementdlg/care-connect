# models/bills_model.py
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional


class Bill(SQLModel, table=True):
    __tablename__ = "bills"

    company_id: UUID = Field(primary_key=True, foreign_key="company_subscriptions.company_id")
    company_subscription_id: UUID = Field(primary_key=True, foreign_key="company_subscriptions.company_subscription_id")
    bill_id: UUID = Field(default_factory=uuid4, primary_key=True)
    file: str = Field(nullable=False, unique=True, max_length=255)
    begin_billing_perdiode_date: datetime = Field(nullable=False)
    end_billing_perdiode_date: datetime = Field(nullable=False, default_factory=datetime.utcnow)
    payed: bool = Field(nullable=False, default=False)