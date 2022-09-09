from sqlalchemy import Column, String
from db.base import Base


class Genres(Base):

    __tablename__ = 'genres'

    id = Column(String(50), nullable=False, primary_key=True)
    name = Column(String(50), nullable=False)
