# schemas/users_schema.py
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime, date
from typing import Optional, List


# Base Schema
class UserBase(BaseModel):
    firstname: str
    lastname: str
    dob: date
    phone: str
    email: str
    password: str
    role: Optional[str] = None
    country: str
    city: str
    street: str
    pc: str
    verified: bool
    stripe_id: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "firstname": "John",
                "lastname": "Doe",
                "dob": "1990-01-01",
                "phone": "+123456789",
                "email": "johndoe@example.com",
                "password": "securepassword123",
                "role": "user",
                "country": "USA",
                "city": "New York",
                "street": "Main Street",
                "pc": "10001",
                "verified": False,
                "stripe_id": "cus_ABCDEF123456",
            }
        }


# Schema for Creating a Single Record
class UserCreate(UserBase):
    pass


# Schema for Reading a Single Record
class UserRead(BaseModel):
    user_id: UUID
    firstname: str
    lastname: str
    dob: date
    phone: str
    email: str
    role: Optional[str] = None
    country: str
    city: str
    street: str
    pc: str
    inscription_date: datetime
    verified: bool
    stripe_id: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "firstname": "John",
                "lastname": "Doe",
                "dob": "1990-01-01",
                "phone": "+123456789",
                "email": "johndoe@example.com",
                "role": "user",
                "country": "USA",
                "city": "New York",
                "street": "Main Street",
                "pc": "10001",
                "inscription_date": "2023-01-15T12:30:00Z",
                "verified": True,
                "stripe_id": "cus_ABCDEF123456",
            }
        }


# Schema for Updating a Record (all fields optional)
class UserUpdate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    dob: Optional[date] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    pc: Optional[str] = None
    verified: Optional[bool] = None
    stripe_id: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "firstname": "Jane",
                "lastname": "Doe",
                "phone": "+987654321",
                "email": "janedoe@example.com",
                "verified": True,
            }
        }


# Schema for Bulk Creating Records
class UserBulkCreate(BaseModel):
    users: List[UserCreate]

    class Config:
        schema_extra = {
            "example": {
                "users": [
                    {
                        "firstname": "John",
                        "lastname": "Doe",
                        "dob": "1990-01-01",
                        "phone": "+123456789",
                        "email": "johndoe@example.com",
                        "password": "securepassword123",
                        "role": "user",
                        "country": "USA",
                        "city": "New York",
                        "street": "Main Street",
                        "pc": "10001",
                        "verified": False,
                        "stripe_id": "cus_ABCDEF123456",
                    },
                    {
                        "firstname": "Alice",
                        "lastname": "Smith",
                        "dob": "1985-07-20",
                        "phone": "+1122334455",
                        "email": "alicesmith@example.com",
                        "password": "anothersecurepassword",
                        "role": "admin",
                        "country": "USA",
                        "city": "Los Angeles",
                        "street": "Second Street",
                        "pc": "90001",
                        "verified": True,
                        "stripe_id": "cus_ZYXWVUT98765",
                    },
                ]
            }
        }