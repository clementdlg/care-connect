# schemas/appointments_schema.py
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List


# Base Schema
class AppointmentBase(BaseModel):
    contractor_id: Optional[UUID] = None
    collaborator_id: Optional[UUID] = None
    appointment_date: datetime
    status: Optional[str] = None
    bill_file: str
    place: str
    note: Optional[int] = None

    class Config:
        schema_extra = {
            "example": {
                "contractor_id": "11111111-2222-3333-4444-555555555555",
                "collaborator_id": "66666666-7777-8888-9999-000000000000",
                "appointment_date": "2023-08-15T14:30:00Z",
                "status": "confirmed",
                "bill_file": "invoice_12345.pdf",
                "place": "Room1",
                "note": 5,
            }
        }


# Schema for Creating a Single Record
class AppointmentCreate(AppointmentBase):
    pass


# Schema for Reading a Single Record
class AppointmentRead(AppointmentBase):
    appointment_id: UUID
    creation_date: datetime

    class Config:
        schema_extra = {
            "example": {
                "appointment_id": "aaabbbcc-dddd-eeee-ffff-111122223333",
                "contractor_id": "11111111-2222-3333-4444-555555555555",
                "collaborator_id": "66666666-7777-8888-9999-000000000000",
                "appointment_date": "2023-08-15T14:30:00Z",
                "creation_date": "2023-08-01T10:00:00Z",
                "status": "confirmed",
                "bill_file": "invoice_12345.pdf",
                "place": "Room1",
                "note": 5,
            }
        }


# Schema for Updating a Record
class AppointmentUpdate(BaseModel):
    contractor_id: Optional[UUID] = None
    collaborator_id: Optional[UUID] = None
    appointment_date: Optional[datetime] = None
    status: Optional[str] = None
    bill_file: Optional[str] = None
    place: Optional[str] = None
    note: Optional[int] = None

    class Config:
        schema_extra = {
            "example": {
                "status": "rescheduled",
                "bill_file": "updated_invoice_12345.pdf",
                "place": "Room2"
            }
        }


# Schema for Bulk Creating Records
class AppointmentBulkCreate(BaseModel):
    appointments: List[AppointmentCreate]

    class Config:
        schema_extra = {
            "example": {
                "appointments": [
                    {
                        "contractor_id": "11111111-2222-3333-4444-555555555555",
                        "collaborator_id": "66666666-7777-8888-9999-000000000000",
                        "appointment_date": "2023-08-15T14:30:00Z",
                        "status": "confirmed",
                        "bill_file": "invoice_12345.pdf",
                        "place": "Room1",
                        "note": 5,
                    },
                    {
                        "contractor_id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
                        "collaborator_id": None,
                        "appointment_date": "2023-09-01T09:00:00Z",
                        "status": "pending",
                        "bill_file": "invoice_67890.pdf",
                        "place": "Room3",
                        "note": 3,
                    }
                ]
            }
        }