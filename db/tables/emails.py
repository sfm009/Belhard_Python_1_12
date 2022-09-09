from sqlalchemy import Column, INT, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base


class Emails(Base):

    __tablename__ = 'emails'

    id = Column(INT, nullable=False, primary_key=True, autoincrement=True)
    email = Column(String(50), nullable=False)
    user_login = Column(String(50), ForeignKey('users.login'), nullable=False)
    users = relationship('Users')

