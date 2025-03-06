# base_queries.py
import os
from sqlmodel import Session, create_engine, SQLModel

DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)

class BaseQuery:
    def __init__(self, session: Session = None):
        self.session = session or Session(engine)
