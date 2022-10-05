from sqlalchemy import Column, INT, String, ForeignKey
from sqlalchemy.orm import relationship

from db.base import Base


class Characters(Base):

    __tablename__ = 'characters'

    id = Column(INT, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    comment = Column(String(50))
    film_id = Column(INT, ForeignKey('persons.id'), nullable=False)
    persons = relationship('Persons')
