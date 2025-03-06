# models/categories_model.py
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from typing import Optional


class Category(SQLModel, table=True):
    __tablename__ = "categories"

    category_id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str = Field(nullable=False, unique=True, max_length=255)
    admin_id: Optional[UUID] = Field(default=None, foreign_key="administrators.admin_id")