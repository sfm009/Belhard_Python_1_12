from sqlalchemy import Column, INT, String, ForeignKey
from sqlalchemy.orm import relationship

from db.base import Base


class Users(Base):

    __tablename__ = 'users'

    login = Column(String(50), nullable=False, primary_key=True)
    password = Column(String(50), nullable=False)
    user_type_id = Column(String(50), ForeignKey('user_types.id'), nullable=False)
    user_types = relationship('UserTypes')
    person_id = Column(INT, ForeignKey('persons.id'), nullable=False)
    persons = relationship('Persons')
