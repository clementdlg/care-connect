# models/posts_model.py
from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime


class Post(SQLModel, table=True):
    __tablename__ = "posts"

    post_id: UUID = Field(default_factory=uuid4, primary_key=True)
    text: str = Field(nullable=False)
    creation_date: datetime = Field(nullable=False, default_factory=datetime.utcnow)
    parent_post_id: Optional[UUID] = Field(default=None, foreign_key="posts.post_id")
    subject_id: UUID = Field(nullable=False, foreign_key="subjects.subject_id")