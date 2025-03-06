# schemas/messages_schema.py
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List


# Base Schema
class MessageBase(BaseModel):
    ticket_id: UUID
    messages_id: UUID
    text: str
    user_id: Optional[UUID] = None
    admin_id: Optional[UUID] = None

    class Config:
        schema_extra = {
            "example": {
                "ticket_id": "11111111-1111-1111-1111-111111111111",
                "messages_id": "22222222-2222-2222-2222-222222222222",
                "text": "This is a sample message text.",
                "user_id": "33333333-3333-3333-3333-333333333333",
                "admin_id": "44444444-4444-4444-4444-444444444444"
            }
        }


# Schema for Creating a Single Record
class MessageCreate(MessageBase):
    pass


# Schema for Reading a Single Record
class MessageRead(MessageBase):
    creation_date: datetime

    class Config:
        schema_extra = {
            "example": {
                "ticket_id": "11111111-1111-1111-1111-111111111111",
                "messages_id": "22222222-2222-2222-2222-222222222222",
                "text": "This is a sample message text.",
                "creation_date": "2023-08-15T12:30:00Z",
                "user_id": "33333333-3333-3333-3333-333333333333",
                "admin_id": "44444444-4444-4444-4444-444444444444"
            }
        }


# Schema for Updating a Record (all fields are optional)
class MessageUpdate(BaseModel):
    text: Optional[str] = None
    user_id: Optional[UUID] = None
    admin_id: Optional[UUID] = None

    class Config:
        schema_extra = {
            "example": {
                "text": "Updated message text",
                "user_id": "33333333-3333-3333-3333-333333333333",
                "admin_id": "44444444-4444-4444-4444-444444444444"
            }
        }


# Schema for Bulk Creating Records
class MessageBulkCreate(BaseModel):
    messages: List[MessageCreate]

    class Config:
        schema_extra = {
            "example": {
                "messages": [
                    {
                        "ticket_id": "11111111-1111-1111-1111-111111111111",
                        "messages_id": "22222222-2222-2222-2222-222222222222",
                        "text": "First sample message",
                        "user_id": "33333333-3333-3333-3333-333333333333",
                        "admin_id": "44444444-4444-4444-4444-444444444444"
                    },
                    {
                        "ticket_id": "55555555-5555-5555-5555-555555555555",
                        "messages_id": "66666666-6666-6666-6666-666666666666",
                        "text": "Second sample message",
                        "user_id": "77777777-7777-7777-7777-777777777777",
                        "admin_id": "88888888-8888-8888-8888-888888888888"
                    }
                ]
            }
        }