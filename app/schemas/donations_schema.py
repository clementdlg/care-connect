# schemas/donations_schema.py
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List


# Base Schema
class DonationBase(BaseModel):
    collaborator_id: UUID
    ngo_id: UUID
    bill_file: str
    amount: int

    class Config:
        schema_extra = {
            "example": {
                "collaborator_id": "11111111-2222-3333-4444-555555555555",
                "ngo_id": "66666666-7777-8888-9999-000000000000",
                "bill_file": "invoice_202308.pdf",
                "amount": 150
            }
        }


# Schema for Creating a Single Record
class DonationCreate(DonationBase):
    pass


# Schema for Reading a Single Record
class DonationRead(DonationBase):
    creation_date: datetime

    class Config:
        schema_extra = {
            "example": {
                "collaborator_id": "11111111-2222-3333-4444-555555555555",
                "ngo_id": "66666666-7777-8888-9999-000000000000",
                "bill_file": "invoice_202308.pdf",
                "amount": 150,
                "creation_date": "2023-08-01T12:00:00Z"
            }
        }


# Schema for Updating a Record
class DonationUpdate(BaseModel):
    collaborator_id: Optional[UUID] = None
    ngo_id: Optional[UUID] = None
    bill_file: Optional[str] = None
    amount: Optional[int] = None

    class Config:
        schema_extra = {
            "example": {
                "bill_file": "updated_invoice_202308.pdf",
                "amount": 175
            }
        }


# Schema for Bulk Creating Records
class DonationBulkCreate(BaseModel):
    donations: List[DonationCreate]

    class Config:
        schema_extra = {
            "example": {
                "donations": [
                    {
                        "collaborator_id": "11111111-2222-3333-4444-555555555555",
                        "ngo_id": "66666666-7777-8888-9999-000000000000",
                        "bill_file": "invoice_202308.pdf",
                        "amount": 150
                    },
                    {
                        "collaborator_id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
                        "ngo_id": "ffffffff-1111-2222-3333-444444444444",
                        "bill_file": "invoice_202309.pdf",
                        "amount": 200
                    }
                ]
            }
        }