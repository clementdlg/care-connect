# schemas/administrators_schema.py
from pydantic import BaseModel
from uuid import UUID
from typing import List, Optional

class AdministratorBase(BaseModel):
    # Optionally, you can set the from_attributes configuration here if you want it applied to all child models.
    class Config:
        from_attributes = True


class AdministratorCreate(AdministratorBase):
    admin_id: UUID

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "admin_id": "123e4567-e89b-12d3-a456-426614174000"
            }
        }


class AdministratorRead(AdministratorBase):
    admin_id: UUID

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "admin_id": "123e4567-e89b-12d3-a456-426614174000"
            }
        }


# Schema for Reading All
class AdministratorBulkRead(AdministratorBase):
    administrators: list[AdministratorRead]
    # If there are no new fields, you may want to inherit Config from the parent,
    # or explicitly set from_attributes = True if needed.
    class Config:
        from_attributes = True


class AdministratorBulkCreate(BaseModel):
    administrators: list[AdministratorCreate]

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "administrators": [
                    {"admin_id": "123e4567-e89b-12d3-a456-426614174000"},
                    {"admin_id": "223e4567-e89b-12d3-a456-426614174111"}
                ]
            }
        }