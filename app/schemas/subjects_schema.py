# schemas/subjects_schema.py
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List


# Base Schema
class SubjectBase(BaseModel):
    collaborator_id: UUID
    title: str
    category_id: UUID

    class Config:
        schema_extra = {
            "example": {
                "collaborator_id": "123e4567-e89b-12d3-a456-426614174000",
                "title": "Introduction to Python",
                "category_id": "223e4567-e89b-12d3-a456-426614174111"
            }
        }


# Schema for Creating a Single Record
class SubjectCreate(SubjectBase):
    pass


# Schema for Reading a Single Record
class SubjectRead(SubjectBase):
    subject_id: UUID
    creation_date: datetime

    class Config:
        schema_extra = {
            "example": {
                "subject_id": "323e4567-e89b-12d3-a456-426614174222",
                "collaborator_id": "123e4567-e89b-12d3-a456-426614174000",
                "title": "Introduction to Python",
                "creation_date": "2023-01-15T12:30:00Z",
                "category_id": "223e4567-e89b-12d3-a456-426614174111"
            }
        }


# Schema for Updating a Record
class SubjectUpdate(BaseModel):
    collaborator_id: Optional[UUID]
    title: Optional[str]
    category_id: Optional[UUID]

    class Config:
        schema_extra = {
            "example": {
                "title": "Advanced Python"
            }
        }


# Schema for Bulk Creating Records
class SubjectBulkCreate(BaseModel):
    subjects: List[SubjectCreate]

    class Config:
        schema_extra = {
            "example": {
                "subjects": [
                    {
                        "collaborator_id": "123e4567-e89b-12d3-a456-426614174000",
                        "title": "Introduction to Python",
                        "category_id": "223e4567-e89b-12d3-a456-426614174111"
                    },
                    {
                        "collaborator_id": "323e4567-e89b-12d3-a456-426614174333",
                        "title": "Data Science Basics",
                        "category_id": "423e4567-e89b-12d3-a456-426614174444"
                    }
                ]
            }
        }