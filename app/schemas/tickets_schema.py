# schemas/tickets_schema.py
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List


# Base Schema
class TicketBase(BaseModel):
    title: str
    text: str
    user_id: UUID
    admin_id: Optional[UUID] = None

    class Config:
        schema_extra = {
            "example": {
                "title": "Issue with Order #1234",
                "text": "I'm having trouble with my recent order.",
                "user_id": "11111111-2222-3333-4444-555555555555",
                "admin_id": "66666666-7777-8888-9999-000000000000"
            }
        }


# Schema for Creating a Single Record
class TicketCreate(TicketBase):
    pass


# Schema for Reading a Single Record
class TicketRead(TicketBase):
    ticket_id: UUID
    open_date: datetime
    close_date: Optional[datetime]

    class Config:
        schema_extra = {
            "example": {
                "ticket_id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
                "title": "Issue with Order #1234",
                "text": "I'm having trouble with my recent order.",
                "open_date": "2023-05-01T12:00:00Z",
                "close_date": None,
                "user_id": "11111111-2222-3333-4444-555555555555",
                "admin_id": "66666666-7777-8888-9999-000000000000"
            }
        }


# Schema for Updating a Record
class TicketUpdate(BaseModel):
    title: Optional[str] = None
    text: Optional[str] = None
    open_date: Optional[datetime] = None
    close_date: Optional[datetime] = None
    user_id: Optional[UUID] = None
    admin_id: Optional[UUID] = None

    class Config:
        schema_extra = {
            "example": {
                "title": "Updated ticket title",
                "text": "Updated details of the issue...",
                "open_date": "2023-05-01T12:00:00Z",
                "close_date": "2023-05-02T15:30:00Z",
                "user_id": "11111111-2222-3333-4444-555555555555",
                "admin_id": "66666666-7777-8888-9999-000000000000"
            }
        }


# Schema for Bulk Creating Records
class TicketBulkCreate(BaseModel):
    tickets: List[TicketCreate]

    class Config:
        schema_extra = {
            "example": {
                "tickets": [
                    {
                        "title": "Issue with Order #1234",
                        "text": "I'm having trouble with my recent order.",
                        "user_id": "11111111-2222-3333-4444-555555555555",
                        "admin_id": "66666666-7777-8888-9999-000000000000"
                    },
                    {
                        "title": "Login failure",
                        "text": "Unable to log in with correct credentials.",
                        "user_id": "22222222-3333-4444-5555-666666666666",
                        "admin_id": None
                    }
                ]
            }
        }