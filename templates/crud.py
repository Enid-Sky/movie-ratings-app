"""CRUD operations"""

from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_movie(title, overview, release_date, poster_path):
    """Creates a movie """

    movie = Movie(title=title, overview=overview,
                  release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie
