# models/administrators_model.py
from sqlmodel import SQLModel, Field
from uuid import uuid4, UUID


class Administrator(SQLModel, table=True):
    __tablename__ = "administrators"

    admin_id: UUID = Field(default_factory=uuid4, primary_key=True, foreign_key="users.user_id")