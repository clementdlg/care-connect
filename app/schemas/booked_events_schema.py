# schemas/booked_events_schema.py
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List


# Base Schema
class BookedEventBase(BaseModel):
    event_id: UUID
    collaborator_id: UUID

    class Config:
        schema_extra = {
            "example": {
                "event_id": "1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
                "collaborator_id": "6d5c4b3a-2f1e-0d9c-8b7a-6f5e4d3c2b1a"
            }
        }


# Schema for Creating a Single Record
class BookedEventCreate(BookedEventBase):
    pass


# Schema for Reading a Single Record
class BookedEventRead(BookedEventBase):
    creation_date: datetime

    class Config:
        schema_extra = {
            "example": {
                "event_id": "1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
                "collaborator_id": "6d5c4b3a-2f1e-0d9c-8b7a-6f5e4d3c2b1a",
                "creation_date": "2023-08-01T12:00:00Z"
            }
        }


# Schema for Updating a Record
class BookedEventUpdate(BaseModel):
    # Primary key fields are not expected to change, so only updatable field is included.
    creation_date: Optional[datetime] = None

    class Config:
        schema_extra = {
            "example": {
                "creation_date": "2023-08-05T14:30:00Z"
            }
        }


# Schema for Bulk Creating Records
class BookedEventBulkCreate(BaseModel):
    booked_events: List[BookedEventCreate]

    class Config:
        schema_extra = {
            "example": {
                "booked_events": [
                    {
                        "event_id": "1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
                        "collaborator_id": "6d5c4b3a-2f1e-0d9c-8b7a-6f5e4d3c2b1a"
                    },
                    {
                        "event_id": "7c8d9e0f-1a2b-3c4d-5e6f-7a8b9c0d1e2f",
                        "collaborator_id": "0f1e2d3c-4b5a-6987-0d9c-8b7a6f5e4d3c"
                    }
                ]
            }
        }