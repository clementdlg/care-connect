# schemas/reports_schema.py
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List


# Base Schema
class ReportBase(BaseModel):
    collaborator_id: Optional[UUID] = None
    title: str
    post_id: Optional[UUID] = None
    subject_id: Optional[UUID] = None
    appointment_id: Optional[UUID] = None

    class Config:
        schema_extra = {
            "example": {
                "collaborator_id": "123e4567-e89b-12d3-a456-426614174001",
                "title": "Monthly Report",
                "post_id": "123e4567-e89b-12d3-a456-426614174002",
                "subject_id": "123e4567-e89b-12d3-a456-426614174003",
                "appointment_id": "123e4567-e89b-12d3-a456-426614174004",
            }
        }


# Schema for Creating a Single Record
class ReportCreate(ReportBase):
    pass


# Schema for Reading a Single Record
class ReportRead(ReportBase):
    report_id: UUID
    creation_date: datetime

    class Config:
        schema_extra = {
            "example": {
                "report_id": "123e4567-e89b-12d3-a456-426614174000",
                "collaborator_id": "123e4567-e89b-12d3-a456-426614174001",
                "title": "Monthly Report",
                "creation_date": "2023-08-01T12:00:00Z",
                "post_id": "123e4567-e89b-12d3-a456-426614174002",
                "subject_id": "123e4567-e89b-12d3-a456-426614174003",
                "appointment_id": "123e4567-e89b-12d3-a456-426614174004",
            }
        }


# Schema for Updating a Record
class ReportUpdate(BaseModel):
    collaborator_id: Optional[UUID] = None
    title: Optional[str] = None
    post_id: Optional[UUID] = None
    subject_id: Optional[UUID] = None
    appointment_id: Optional[UUID] = None

    class Config:
        schema_extra = {
            "example": {
                "title": "Updated Monthly Report",
                "collaborator_id": "123e4567-e89b-12d3-a456-426614174001",
            }
        }


# Schema for Bulk Creating Records
class ReportBulkCreate(BaseModel):
    reports: List[ReportCreate]

    class Config:
        schema_extra = {
            "example": {
                "reports": [
                    {
                        "collaborator_id": "123e4567-e89b-12d3-a456-426614174001",
                        "title": "Monthly Report",
                        "post_id": "123e4567-e89b-12d3-a456-426614174002",
                        "subject_id": "123e4567-e89b-12d3-a456-426614174003",
                        "appointment_id": "123e4567-e89b-12d3-a456-426614174004",
                    },
                    {
                        "collaborator_id": "223e4567-e89b-12d3-a456-426614174005",
                        "title": "Weekly Summary",
                        "post_id": None,
                        "subject_id": None,
                        "appointment_id": "223e4567-e89b-12d3-a456-426614174006",
                    }
                ]
            }
        }