# schemas/companies_schema.py
from pydantic import BaseModel
from uuid import UUID
from datetime import date
from typing import Optional, List


# Base Schema
class CompanyBase(BaseModel):
    name: str
    website: Optional[str] = None
    registration_number: str
    registration_date: date
    industry: str
    revenue: int
    size: int
    admin_id: Optional[UUID] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Example Company",
                "website": "https://www.example.com",
                "registration_number": "REG12345",
                "registration_date": "2023-01-01",
                "industry": "Technology",
                "revenue": 1000000,
                "size": 500,
                "admin_id": "44444444-4444-4444-4444-444444444444",
            }
        }


# Schema for Creating a Single Record
class CompanyCreate(CompanyBase):
    pass


# Schema for Reading a Single Record
class CompanyRead(CompanyBase):
    company_id: UUID

    class Config:
        schema_extra = {
            "example": {
                "company_id": "11111111-1111-1111-1111-111111111111",
                "name": "Example Company",
                "website": "https://www.example.com",
                "registration_number": "REG12345",
                "registration_date": "2023-01-01",
                "industry": "Technology",
                "revenue": 1000000,
                "size": 500,
                "admin_id": "44444444-4444-4444-4444-444444444444",
            }
        }


# Schema for Updating a Record
class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    website: Optional[str] = None
    registration_number: Optional[str] = None
    registration_date: Optional[date] = None
    industry: Optional[str] = None
    revenue: Optional[int] = None
    size: Optional[int] = None
    admin_id: Optional[UUID] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Updated Company Name",
                "website": "https://www.updated.com",
                "registration_number": "REG98765",
                "registration_date": "2023-05-05",
                "industry": "Healthcare",
                "revenue": 2000000,
                "size": 600,
                "admin_id": "55555555-5555-5555-5555-555555555555",
            }
        }


# Schema for Bulk Creating Records
class CompanyBulkCreate(BaseModel):
    companies: List[CompanyCreate]

    class Config:
        schema_extra = {
            "example": {
                "companies": [
                    {
                        "name": "Example Company",
                        "website": "https://www.example.com",
                        "registration_number": "REG12345",
                        "registration_date": "2023-01-01",
                        "industry": "Technology",
                        "revenue": 1000000,
                        "size": 500,
                        "admin_id": "44444444-4444-4444-4444-444444444444"
                    },
                    {
                        "name": "Another Company",
                        "website": "https://www.another.com",
                        "registration_number": "REG67890",
                        "registration_date": "2023-02-01",
                        "industry": "Finance",
                        "revenue": 500000,
                        "size": 200,
                        "admin_id": "66666666-6666-6666-6666-666666666666"
                    }
                ]
            }
        }