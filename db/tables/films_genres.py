from sqlalchemy import Column, INT, String, ForeignKey
from sqlalchemy.orm import relationship

from db.base import Base


class FilmsGenres(Base):

    __tablename__ = 'films_genres'

    film_id = Column(INT, ForeignKey('films.id'), nullable=False)
    films = relationship('Films')
    fil_genre_id = Column(String(50), ForeignKey('genres.id'), nullable=False)
    genres = relationship('Genres')
