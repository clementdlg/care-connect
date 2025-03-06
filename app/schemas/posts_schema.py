# schemas/posts_schema.py
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List


# Base Schema
class PostBase(BaseModel):
    text: str
    parent_post_id: Optional[UUID] = None
    subject_id: UUID

    class Config:
        schema_extra = {
            "example": {
                "text": "This is a sample post content",
                "parent_post_id": "e7c8d1b2-3c64-4f6c-a6f5-123456789abc",
                "subject_id": "a1b2c3d4-5678-90ab-cdef-1234567890ab"
            }
        }


# Schema for Creating a Single Record
class PostCreate(PostBase):
    pass


# Schema for Reading a Single Record
class PostRead(PostBase):
    post_id: UUID
    creation_date: datetime

    class Config:
        schema_extra = {
            "example": {
                "post_id": "f1e2d3c4-b5a6-7890-1234-56789abcdef0",
                "text": "This is a sample post content",
                "creation_date": "2023-08-15T12:00:00Z",
                "parent_post_id": "e7c8d1b2-3c64-4f6c-a6f5-123456789abc",
                "subject_id": "a1b2c3d4-5678-90ab-cdef-1234567890ab"
            }
        }


# Schema for Updating a Record
class PostUpdate(BaseModel):
    text: Optional[str] = None
    parent_post_id: Optional[UUID] = None
    subject_id: Optional[UUID] = None

    class Config:
        schema_extra = {
            "example": {
                "text": "Updated post content",
                "parent_post_id": "e7c8d1b2-3c64-4f6c-a6f5-123456789abc",
                "subject_id": "a1b2c3d4-5678-90ab-cdef-1234567890ab"
            }
        }


# Schema for Bulk Creating Records
class PostBulkCreate(BaseModel):
    posts: List[PostCreate]

    class Config:
        schema_extra = {
            "example": {
                "posts": [
                    {
                        "text": "This is a sample post content for bulk create",
                        "parent_post_id": "e7c8d1b2-3c64-4f6c-a6f5-123456789abc",
                        "subject_id": "a1b2c3d4-5678-90ab-cdef-1234567890ab"
                    },
                    {
                        "text": "Another sample post content",
                        "parent_post_id": None,
                        "subject_id": "b2c3d4e5-6789-0abc-def1-234567890abc"
                    }
                ]
            }
        }