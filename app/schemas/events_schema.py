# schemas/events_schema.py
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List


# Base Schema
class EventBase(BaseModel):
    begin_at: datetime
    end_at: datetime
    place: str
    title: str
    capacity: int
    ngo_id: Optional[UUID] = None
    admin_id: Optional[UUID] = None

    class Config:
        schema_extra = {
            "example": {
                "begin_at": "2023-09-01T10:00:00Z",
                "end_at": "2023-09-01T12:00:00Z",
                "place": "Community Center",
                "title": "Charity Event",
                "capacity": 100,
                "ngo_id": "123e4567-e89b-12d3-a456-426614174000",
                "admin_id": "123e4567-e89b-12d3-a456-426614174111"
            }
        }


# Schema for Creating a Single Record
class EventCreate(EventBase):
    pass


# Schema for Reading a Single Record
class EventRead(EventBase):
    event_id: UUID
    created_at: datetime

    class Config:
        schema_extra = {
            "example": {
                "event_id": "123e4567-e89b-12d3-a456-426614174222",
                "created_at": "2023-08-15T09:30:00Z",
                "begin_at": "2023-09-01T10:00:00Z",
                "end_at": "2023-09-01T12:00:00Z",
                "place": "Community Center",
                "title": "Charity Event",
                "capacity": 100,
                "ngo_id": "123e4567-e89b-12d3-a456-426614174000",
                "admin_id": "123e4567-e89b-12d3-a456-426614174111"
            }
        }


# Schema for Updating a Record
class EventUpdate(BaseModel):
    begin_at: Optional[datetime]
    end_at: Optional[datetime]
    place: Optional[str]
    title: Optional[str]
    capacity: Optional[int]
    ngo_id: Optional[UUID]
    admin_id: Optional[UUID]

    class Config:
        schema_extra = {
            "example": {
                "place": "Updated Venue",
                "capacity": 120
            }
        }


# Schema for Bulk Creating Records
class EventBulkCreate(BaseModel):
    events: List[EventCreate]

    class Config:
        schema_extra = {
            "example": {
                "events": [
                    {
                        "begin_at": "2023-09-01T10:00:00Z",
                        "end_at": "2023-09-01T12:00:00Z",
                        "place": "Community Center",
                        "title": "Charity Event",
                        "capacity": 100,
                        "ngo_id": "123e4567-e89b-12d3-a456-426614174000",
                        "admin_id": "123e4567-e89b-12d3-a456-426614174111"
                    },
                    {
                        "begin_at": "2023-09-05T14:00:00Z",
                        "end_at": "2023-09-05T16:00:00Z",
                        "place": "Local Park",
                        "title": "Community Meetup",
                        "capacity": 50,
                        "ngo_id": "123e4567-e89b-12d3-a456-426614174333",
                        "admin_id": "123e4567-e89b-12d3-a456-426614174444"
                    }
                ]
            }
        }