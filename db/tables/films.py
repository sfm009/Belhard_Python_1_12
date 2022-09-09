from sqlalchemy import Column, INT, String, DATETIME, ForeignKey, FLOAT
from sqlalchemy.orm import relationship

from db.base import Base


class Films(Base):

    __tablename__ = 'films'

    id = Column(INT, nullable=False, primary_key=True, autoincrement=True)
    duration = Column(INT, nullable=False)
    name = Column(String(50), nullable=False)
    release_date = Column(DATETIME, nullable=False)
    rating = Column(FLOAT, nullable=False)
    director_id = Column(INT, ForeignKey('persons.id'), nullable=False)
    persons = relationship('Persons')
