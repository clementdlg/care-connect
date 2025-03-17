# administrator_queries.py
from uuid import UUID
from sqlmodel import select
from models.administrators_model import Administrator
from schemas.administrators_schema import (
    AdministratorCreate,
    AdministratorRead,
    AdministratorBulkRead,
    AdministratorBulkCreate
)
from .base_queries import BaseQuery


class AdministratorQuery(BaseQuery):
    def get_by_id(self, admin_id: UUID) -> AdministratorRead | None:
        """
        Récupère un administrateur par son identifiant.
        """
        statement = select(Administrator).where(Administrator.admin_id == admin_id)
        admin = self.session.exec(statement).first()
        if admin:
            return AdministratorRead.from_orm(admin)
        return None

    def get_all(self) -> list[AdministratorBulkRead]:
        """
        Récupère tous les administrateurs.
        """
        statement = select(Administrator)
        admins = self.session.exec(statement).all()
        return admins


              

    def create(self, admin_data: AdministratorCreate) -> AdministratorRead:
        """
        Crée un nouvel administrateur.
        """
        admin = Administrator(admin_id=admin_data.admin_id)
        self.session.add(admin)
        self.session.commit()
        self.session.refresh(admin)
        return AdministratorRead.from_orm(admin)

    def bulk_create(self, bulk_data: AdministratorBulkCreate) -> list[AdministratorRead]:
        """
        Crée plusieurs administrateurs en une seule opération.
        """
        admins = [Administrator(admin_id=admin.admin_id) for admin in bulk_data.administrators]
        self.session.add_all(admins)
        self.session.commit()
        for admin in admins:
            self.session.refresh(admin)
        return [AdministratorRead.from_orm(admin) for admin in admins]
