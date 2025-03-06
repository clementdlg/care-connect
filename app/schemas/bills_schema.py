# schemas/bills_schema.py
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List


# Base Schema
class BillBase(BaseModel):
    file: str
    begin_billing_perdiode_date: datetime
    end_billing_perdiode_date: datetime
    payed: bool

    class Config:
        schema_extra = {
            "example": {
                "file": "bill_march.pdf",
                "begin_billing_perdiode_date": "2023-03-01T00:00:00Z",
                "end_billing_perdiode_date": "2023-03-31T23:59:59Z",
                "payed": False
            }
        }


# Schema for Creating a Single Record
class BillCreate(BillBase):
    company_id: UUID
    company_subscription_id: UUID

    class Config:
        schema_extra = {
            "example": {
                "company_id": "123e4567-e89b-12d3-a456-426614174000",
                "company_subscription_id": "223e4567-e89b-12d3-a456-426614174001",
                "file": "bill_march.pdf",
                "begin_billing_perdiode_date": "2023-03-01T00:00:00Z",
                "end_billing_perdiode_date": "2023-03-31T23:59:59Z",
                "payed": False
            }
        }


# Schema for Reading a Single Record
class BillRead(BillBase):
    company_id: UUID
    company_subscription_id: UUID
    bill_id: UUID

    class Config:
        schema_extra = {
            "example": {
                "company_id": "123e4567-e89b-12d3-a456-426614174000",
                "company_subscription_id": "223e4567-e89b-12d3-a456-426614174001",
                "bill_id": "323e4567-e89b-12d3-a456-426614174002",
                "file": "bill_march.pdf",
                "begin_billing_perdiode_date": "2023-03-01T00:00:00Z",
                "end_billing_perdiode_date": "2023-03-31T23:59:59Z",
                "payed": False
            }
        }


# Schema for Updating a Record
class BillUpdate(BaseModel):
    file: Optional[str] = None
    begin_billing_perdiode_date: Optional[datetime] = None
    end_billing_perdiode_date: Optional[datetime] = None
    payed: Optional[bool] = None

    class Config:
        schema_extra = {
            "example": {
                "file": "updated_bill_march.pdf",
                "begin_billing_perdiode_date": "2023-03-01T01:00:00Z",
                "end_billing_perdiode_date": "2023-03-31T23:00:00Z",
                "payed": True
            }
        }


# Schema for Bulk Creating Records
class BillBulkCreate(BaseModel):
    bills: List[BillCreate]

    class Config:
        schema_extra = {
            "example": {
                "bills": [
                    {
                        "company_id": "123e4567-e89b-12d3-a456-426614174000",
                        "company_subscription_id": "223e4567-e89b-12d3-a456-426614174001",
                        "file": "bill_march.pdf",
                        "begin_billing_perdiode_date": "2023-03-01T00:00:00Z",
                        "end_billing_perdiode_date": "2023-03-31T23:59:59Z",
                        "payed": False
                    },
                    {
                        "company_id": "223e4567-e89b-12d3-a456-426614174111",
                        "company_subscription_id": "323e4567-e89b-12d3-a456-426614174112",
                        "file": "bill_april.pdf",
                        "begin_billing_perdiode_date": "2023-04-01T00:00:00Z",
                        "end_billing_perdiode_date": "2023-04-30T23:59:59Z",
                        "payed": True
                    }
                ]
            }
        }