# schemas/packs_schema.py
from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from datetime import datetime


# Base Schema
class PackBase(BaseModel):
    name: str
    activity_number: int
    annual_collaborator_price: int
    bonus_consultation_price: int
    default_consultation_number: int
    chatbot_messages_number: Optional[int]
    admin_id: UUID

    class Config:
        schema_extra = {
            "example": {
                "name": "Basic Pack",
                "activity_number": 10,
                "annual_collaborator_price": 100,
                "bonus_consultation_price": 50,
                "default_consultation_number": 5,
                "chatbot_messages_number": 20,
                "admin_id": "123e4567-e89b-12d3-a456-426614174000",
            }
        }


# Schema for Creating a Single Record
class PackCreate(PackBase):
    pass


# Schema for Reading a Single Record
class PackRead(PackBase):
    pack_id: UUID
    creation_date: datetime

    class Config:
        schema_extra = {
            "example": {
                "pack_id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
                "name": "Basic Pack",
                "activity_number": 10,
                "annual_collaborator_price": 100,
                "bonus_consultation_price": 50,
                "default_consultation_number": 5,
                "chatbot_messages_number": 20,
                "admin_id": "123e4567-e89b-12d3-a456-426614174000",
                "creation_date": "2023-01-15T12:30:00Z",
            }
        }


# Schema for Updating a Record
class PackUpdate(BaseModel):
    name: Optional[str] = None
    activity_number: Optional[int] = None
    annual_collaborator_price: Optional[int] = None
    bonus_consultation_price: Optional[int] = None
    default_consultation_number: Optional[int] = None
    chatbot_messages_number: Optional[int] = None
    admin_id: Optional[UUID] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Updated Pack Name",
                "activity_number": 15,
                "annual_collaborator_price": 120,
                "bonus_consultation_price": 60,
                "default_consultation_number": 6,
                "chatbot_messages_number": 25,
                "admin_id": "123e4567-e89b-12d3-a456-426614174000",
            }
        }


# Schema for Bulk Creating Records
class PackBulkCreate(BaseModel):
    packs: List[PackCreate]

    class Config:
        schema_extra = {
            "example": {
                "packs": [
                    {
                        "name": "Basic Pack",
                        "activity_number": 10,
                        "annual_collaborator_price": 100,
                        "bonus_consultation_price": 50,
                        "default_consultation_number": 5,
                        "chatbot_messages_number": 20,
                        "admin_id": "123e4567-e89b-12d3-a456-426614174000",
                    },
                    {
                        "name": "Premium Pack",
                        "activity_number": 20,
                        "annual_collaborator_price": 200,
                        "bonus_consultation_price": 80,
                        "default_consultation_number": 10,
                        "chatbot_messages_number": 40,
                        "admin_id": "223e4567-e89b-12d3-a456-426614174111",
                    },
                ]
            }
        }