from sqlalchemy import Column, INT, String, DATETIME

from db.base import Base


class Persons(Base):

    __tablename__ = 'persons'

    id = Column(INT, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    birth_date = Column(DATETIME, nullable=False)
