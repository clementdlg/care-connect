# schemas/estimates_schema.py
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List


# Base Schema
class EstimateBase(BaseModel):
    file: str
    signature_date: Optional[datetime] = None

    class Config:
        schema_extra = {
            "example": {
                "file": "invoice_2023.pdf",
                "signature_date": "2023-03-15T10:15:00Z"
            }
        }


# Schema for Creating a Single Record
class EstimateCreate(EstimateBase):
    company_id: UUID
    company_subscription_id: UUID

    class Config:
        schema_extra = {
            "example": {
                "company_id": "123e4567-e89b-12d3-a456-426614174000",
                "company_subscription_id": "223e4567-e89b-12d3-a456-426614174001",
                "file": "invoice_2023.pdf",
                "signature_date": "2023-03-15T10:15:00Z"
            }
        }


# Schema for Reading a Single Record
class EstimateRead(EstimateBase):
    company_id: UUID
    company_subscription_id: UUID
    creation_date: datetime

    class Config:
        schema_extra = {
            "example": {
                "company_id": "123e4567-e89b-12d3-a456-426614174000",
                "company_subscription_id": "223e4567-e89b-12d3-a456-426614174001",
                "file": "invoice_2023.pdf",
                "creation_date": "2023-03-15T09:00:00Z",
                "signature_date": "2023-03-15T10:15:00Z"
            }
        }


# Schema for Updating a Record
class EstimateUpdate(BaseModel):
    file: Optional[str] = None
    signature_date: Optional[datetime] = None

    class Config:
        schema_extra = {
            "example": {
                "file": "updated_invoice_2023.pdf",
                "signature_date": "2023-03-16T11:00:00Z"
            }
        }


# Schema for Bulk Creating Records
class EstimateBulkCreate(BaseModel):
    estimates: List[EstimateCreate]

    class Config:
        schema_extra = {
            "example": {
                "estimates": [
                    {
                        "company_id": "123e4567-e89b-12d3-a456-426614174000",
                        "company_subscription_id": "223e4567-e89b-12d3-a456-426614174001",
                        "file": "invoice_2023.pdf",
                        "signature_date": "2023-03-15T10:15:00Z"
                    },
                    {
                        "company_id": "323e4567-e89b-12d3-a456-426614174222",
                        "company_subscription_id": "423e4567-e89b-12d3-a456-426614174333",
                        "file": "invoice_2023_B.pdf",
                        "signature_date": "2023-03-16T11:00:00Z"
                    }
                ]
            }
        }