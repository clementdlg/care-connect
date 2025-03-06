# schemas/contracts_schema.py
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List


# Base Schema
class ContractBase(BaseModel):
    file: str
    signature_date: Optional[datetime] = None

    class Config:
        schema_extra = {
            "example": {
                "file": "contract_agreement.pdf",
                "signature_date": "2023-05-15T10:30:00Z"
            }
        }


# Schema for Creating a Single Record
class ContractCreate(ContractBase):
    company_id: UUID
    company_subscription_id: UUID

    class Config:
        schema_extra = {
            "example": {
                "company_id": "123e4567-e89b-12d3-a456-426614174000",
                "company_subscription_id": "223e4567-e89b-12d3-a456-426614174001",
                "file": "contract_agreement.pdf",
                "signature_date": "2023-05-15T10:30:00Z"
            }
        }


# Schema for Reading a Single Record
class ContractRead(ContractBase):
    company_id: UUID
    company_subscription_id: UUID
    creation_date: datetime

    class Config:
        schema_extra = {
            "example": {
                "company_id": "123e4567-e89b-12d3-a456-426614174000",
                "company_subscription_id": "223e4567-e89b-12d3-a456-426614174001",
                "file": "contract_agreement.pdf",
                "creation_date": "2023-05-01T09:00:00Z",
                "signature_date": "2023-05-15T10:30:00Z"
            }
        }


# Schema for Updating a Record
class ContractUpdate(BaseModel):
    file: Optional[str] = None
    signature_date: Optional[datetime] = None

    class Config:
        schema_extra = {
            "example": {
                "file": "updated_contract.pdf",
                "signature_date": "2023-05-20T11:00:00Z"
            }
        }


# Schema for Bulk Creating Records
class ContractBulkCreate(BaseModel):
    contracts: List[ContractCreate]

    class Config:
        schema_extra = {
            "example": {
                "contracts": [
                    {
                        "company_id": "123e4567-e89b-12d3-a456-426614174000",
                        "company_subscription_id": "223e4567-e89b-12d3-a456-426614174001",
                        "file": "contract_agreement.pdf",
                        "signature_date": "2023-05-15T10:30:00Z"
                    },
                    {
                        "company_id": "323e4567-e89b-12d3-a456-426614174222",
                        "company_subscription_id": "423e4567-e89b-12d3-a456-426614174333",
                        "file": "contract_proposal.pdf",
                        "signature_date": "2023-06-01T08:45:00Z"
                    }
                ]
            }
        }