from sqlalchemy import Column, String

from db.base import Base


class UserTypes(Base):

    __tablename__ = 'user_types'

    id = Column(String(50), nullable=False, primary_key=True)
    name = Column(String(50), nullable=False)
