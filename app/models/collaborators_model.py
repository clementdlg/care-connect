# models/collaborators_model.py
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4


class Collaborator(SQLModel, table=True):
    __tablename__ = "collaborators"

    collaborator_id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        foreign_key="users.user_id"
    )
    company_id: UUID = Field(
        nullable=False,
        foreign_key="companies.company_id"
    )