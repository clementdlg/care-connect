# models/users_model.py
from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import uuid4, UUID
from datetime import datetime, date


class User(SQLModel, table=True):
    __tablename__ = "users"

    user_id: UUID = Field(default_factory=uuid4, primary_key=True)
    firstname: str = Field(nullable=False, max_length=50)
    lastname: str = Field(nullable=False, max_length=50)
    dob: date = Field(nullable=False)
    phone: str = Field(nullable=False, unique=True, max_length=50)
    email: str = Field(nullable=False, unique=True, max_length=255)
    password: str = Field(nullable=False, max_length=128)
    role: Optional[str] = Field(default=None, max_length=50)
    country: str = Field(nullable=False, max_length=255)
    city: str = Field(nullable=False, max_length=255)
    street: str = Field(nullable=False, max_length=255)
    pc: str = Field(nullable=False, max_length=10)
    inscription_date: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    verified: bool = Field(nullable=False)
    stripe_id: Optional[str] = Field(default=None, unique=True, max_length=255)