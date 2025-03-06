# routes/administrator_routes.py
from fastapi import APIRouter, HTTPException
from uuid import UUID
from sqlmodel import Session
from queries.administrator_queries import AdministratorQuery
from queries.base_queries import engine
from schemas.administrators_schema import AdministratorCreate, AdministratorBulkCreate

router = APIRouter()


@router.get("/")
def get_all_administrators():
    with Session(engine) as session:
        admin_queries = AdministratorQuery(session)
        admins = admin_queries.get_all()
        return [admin.dict() for admin in admins]


@router.get("/{admin_id}")
def get_administrator(admin_id: UUID):
    with Session(engine) as session:
        admin_queries = AdministratorQuery(session)
        admin = admin_queries.get_by_id(admin_id)
        if admin is None:
            raise HTTPException(status_code=404, detail="Administrator not found")
        return admin.dict()


@router.post("/")
def create_administrator(admin_create: AdministratorCreate):
    with Session(engine) as session:
        admin_queries = AdministratorQuery(session)
        admin = admin_queries.create(admin_create)
        return admin.dict()


@router.post("/bulk")
def create_bulk_administrators(bulk_create: AdministratorBulkCreate):
    with Session(engine) as session:
        admin_queries = AdministratorQuery(session)
        admins = admin_queries.bulk_create(bulk_create)
        return [admin.dict() for admin in admins]