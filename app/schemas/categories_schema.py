# schemas/categories_schema.py
from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List


# Base Schema
class CategoryBase(BaseModel):
    title: str
    admin_id: Optional[UUID] = None

    class Config:
        schema_extra = {
            "example": {
                "title": "Electronics",
                "admin_id": "123e4567-e89b-12d3-a456-426614174000"
            }
        }


# Schema for Creating a Single Record
class CategoryCreate(CategoryBase):
    pass


# Schema for Reading a Single Record
class CategoryRead(CategoryBase):
    category_id: UUID

    class Config:
        schema_extra = {
            "example": {
                "category_id": "123e4567-e89b-12d3-a456-426614174000",
                "title": "Electronics",
                "admin_id": "123e4567-e89b-12d3-a456-426614174000"
            }
        }


# Schema for Updating a Record
class CategoryUpdate(BaseModel):
    title: Optional[str] = None
    admin_id: Optional[UUID] = None

    class Config:
        schema_extra = {
            "example": {
                "title": "Updated Electronics",
                "admin_id": "123e4567-e89b-12d3-a456-426614174000"
            }
        }


# Schema for Bulk Creating Records
class CategoryBulkCreate(BaseModel):
    categories: List[CategoryCreate]

    class Config:
        schema_extra = {
            "example": {
                "categories": [
                    {"title": "Electronics", "admin_id": "123e4567-e89b-12d3-a456-426614174000"},
                    {"title": "Appliances", "admin_id": "223e4567-e89b-12d3-a456-426614174000"}
                ]
            }
        }