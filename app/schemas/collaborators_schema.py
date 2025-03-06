# schemas/collaborators_schema.py
from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List


# Base Schema
class CollaboratorBase(BaseModel):
    company_id: UUID

    class Config:
        schema_extra = {
            "example": {
                "company_id": "123e4567-e89b-12d3-a456-426614174000"
            }
        }


# Schema for Creating a Single Record
class CollaboratorCreate(CollaboratorBase):
    pass


# Schema for Reading a Single Record
class CollaboratorRead(CollaboratorBase):
    collaborator_id: UUID

    class Config:
        schema_extra = {
            "example": {
                "collaborator_id": "223e4567-e89b-12d3-a456-426614174111",
                "company_id": "123e4567-e89b-12d3-a456-426614174000"
            }
        }


# Schema for Updating a Record
class CollaboratorUpdate(BaseModel):
    company_id: Optional[UUID]

    class Config:
        schema_extra = {
            "example": {
                "company_id": "323e4567-e89b-12d3-a456-426614174222"
            }
        }


# Schema for Bulk Creating Records
class CollaboratorBulkCreate(BaseModel):
    collaborators: List[CollaboratorCreate]

    class Config:
        schema_extra = {
            "example": {
                "collaborators": [
                    {"company_id": "123e4567-e89b-12d3-a456-426614174000"},
                    {"company_id": "223e4567-e89b-12d3-a456-426614174111"}
                ]
            }
        }