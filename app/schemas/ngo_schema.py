# schemas/ngo_schema.py
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List


# Base Schema
class NgoBase(BaseModel):
    name: str
    registration_number: str
    registration_date: datetime
    address: str
    country: str
    type: str
    presentation: str
    website: str
    phone: str
    stripe_id: Optional[str] = None
    admin_id: Optional[UUID] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Helping Hands",
                "registration_number": "REG123456",
                "registration_date": "2023-10-01T09:30:00Z",
                "address": "123 Charity Lane",
                "country": "USA",
                "type": "Non-profit",
                "presentation": "We are dedicated to making the world a better place.",
                "website": "https://www.helpinghands.org",
                "phone": "+1-555-1234",
                "stripe_id": "stripe_987654321",
                "admin_id": "123e4567-e89b-12d3-a456-426614174000"
            }
        }


# Schema for Creating a Single Record
class NgoCreate(NgoBase):
    pass


# Schema for Reading a Single Record
class NgoRead(NgoBase):
    ngo_id: UUID

    class Config:
        schema_extra = {
            "example": {
                "ngo_id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "Helping Hands",
                "registration_number": "REG123456",
                "registration_date": "2023-10-01T09:30:00Z",
                "address": "123 Charity Lane",
                "country": "USA",
                "type": "Non-profit",
                "presentation": "We are dedicated to making the world a better place.",
                "website": "https://www.helpinghands.org",
                "phone": "+1-555-1234",
                "stripe_id": "stripe_987654321",
                "admin_id": "123e4567-e89b-12d3-a456-426614174000"
            }
        }


# Schema for Updating a Record
class NgoUpdate(BaseModel):
    name: Optional[str] = None
    registration_number: Optional[str] = None
    registration_date: Optional[datetime] = None
    address: Optional[str] = None
    country: Optional[str] = None
    type: Optional[str] = None
    presentation: Optional[str] = None
    website: Optional[str] = None
    phone: Optional[str] = None
    stripe_id: Optional[str] = None
    admin_id: Optional[UUID] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "New Helping Hands",
                "registration_number": "REG654321",
                "registration_date": "2023-11-01T10:00:00Z",
                "address": "456 New Charity Lane",
                "country": "USA",
                "type": "Charity",
                "presentation": "Updated presentation text here.",
                "website": "https://www.newhelpinghands.org",
                "phone": "+1-555-5678",
                "stripe_id": "stripe_123456789",
                "admin_id": "223e4567-e89b-12d3-a456-426614174000"
            }
        }


# Schema for Bulk Creating Records
class NgoBulkCreate(BaseModel):
    ngos: List[NgoCreate]

    class Config:
        schema_extra = {
            "example": {
                "ngos": [
                    {
                        "name": "Helping Hands",
                        "registration_number": "REG123456",
                        "registration_date": "2023-10-01T09:30:00Z",
                        "address": "123 Charity Lane",
                        "country": "USA",
                        "type": "Non-profit",
                        "presentation": "We are dedicated to making the world a better place.",
                        "website": "https://www.helpinghands.org",
                        "phone": "+1-555-1234",
                        "stripe_id": "stripe_987654321",
                        "admin_id": "123e4567-e89b-12d3-a456-426614174000"
                    },
                    {
                        "name": "Hope Foundation",
                        "registration_number": "REG654321",
                        "registration_date": "2023-09-15T08:00:00Z",
                        "address": "789 Hope Street",
                        "country": "USA",
                        "type": "Charity",
                        "presentation": "Committed to giving hope to those in need.",
                        "website": "https://www.hopefoundation.org",
                        "phone": "+1-555-6789",
                        "stripe_id": "stripe_123456789",
                        "admin_id": "223e4567-e89b-12d3-a456-426614174000"
                    }
                ]
            }
        }