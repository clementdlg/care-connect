# schemas/company_subscriptions_schema.py
from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List


# Base Schema
class CompanySubscriptionBase(BaseModel):
    bonus_consultation_number: int
    billing_plan: str
    status: Optional[str] = None
    pack_id: UUID

    class Config:
        schema_extra = {
            "example": {
                "bonus_consultation_number": 5,
                "billing_plan": "Basic",
                "status": "active",
                "pack_id": "223e4567-e89b-12d3-a456-426614174001"
            }
        }


# Schema for Creating a Single Record
class CompanySubscriptionCreate(CompanySubscriptionBase):
    company_id: UUID

    class Config:
        schema_extra = {
            "example": {
                "company_id": "123e4567-e89b-12d3-a456-426614174000",
                "bonus_consultation_number": 5,
                "billing_plan": "Basic",
                "status": "active",
                "pack_id": "223e4567-e89b-12d3-a456-426614174001"
            }
        }


# Schema for Reading a Single Record
class CompanySubscriptionRead(CompanySubscriptionBase):
    company_id: UUID
    company_subscription_id: UUID

    class Config:
        schema_extra = {
            "example": {
                "company_id": "123e4567-e89b-12d3-a456-426614174000",
                "company_subscription_id": "323e4567-e89b-12d3-a456-426614174222",
                "bonus_consultation_number": 5,
                "billing_plan": "Basic",
                "status": "active",
                "pack_id": "223e4567-e89b-12d3-a456-426614174001"
            }
        }


# Schema for Updating a Record
class CompanySubscriptionUpdate(BaseModel):
    bonus_consultation_number: Optional[int] = None
    billing_plan: Optional[str] = None
    status: Optional[str] = None
    pack_id: Optional[UUID] = None

    class Config:
        schema_extra = {
            "example": {
                "bonus_consultation_number": 8,
                "billing_plan": "Premium",
                "status": "paused",
                "pack_id": "323e4567-e89b-12d3-a456-426614174333"
            }
        }


# Schema for Bulk Creating Records
class CompanySubscriptionBulkCreate(BaseModel):
    company_subscriptions: List[CompanySubscriptionCreate]

    class Config:
        schema_extra = {
            "example": {
                "company_subscriptions": [
                    {
                        "company_id": "123e4567-e89b-12d3-a456-426614174000",
                        "bonus_consultation_number": 5,
                        "billing_plan": "Basic",
                        "status": "active",
                        "pack_id": "223e4567-e89b-12d3-a456-426614174001"
                    },
                    {
                        "company_id": "223e4567-e89b-12d3-a456-426614174111",
                        "bonus_consultation_number": 10,
                        "billing_plan": "Premium",
                        "status": "active",
                        "pack_id": "323e4567-e89b-12d3-a456-426614174222"
                    }
                ]
            }
        }