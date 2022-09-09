from sqlalchemy import Column, INT, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base


class UserFavoriteFilms(Base):

    __tablename__ = 'user_favorite_films'

    user_login = Column(String(50), ForeignKey('users.login'), nullable=False)
    users = relationship('Users')
    fil_id = Column(INT, ForeignKey('films.id'), nullable=False)
    films = relationship('Films')
