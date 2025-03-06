# models/subjects_model.py
from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime


class Subject(SQLModel, table=True):
    __tablename__ = "subjects"

    subject_id: UUID = Field(default_factory=uuid4, primary_key=True)
    collaborator_id: UUID = Field(nullable=False, foreign_key="collaborators.collaborator_id")
    title: str = Field(nullable=False, unique=True, max_length=255)
    creation_date: datetime = Field(nullable=False, default_factory=datetime.utcnow)
    category_id: UUID = Field(nullable=False, foreign_key="categories.category_id")