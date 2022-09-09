from sqlalchemy import Column, INT, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base


class CharactersActors(Base):

    __tablename__ = 'characters_actors'

    character_id = Column(INT, ForeignKey('characters.id'), nullable=False)
    characters = relationship('Characters')
    person_id = Column(INT, ForeignKey('persons.id'), nullable=False)
    persons = relationship('Pesrons')
