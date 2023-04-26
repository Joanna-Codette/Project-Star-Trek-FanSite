"""CRUD operations."""

from model import db, User, Movie, Rating, Review, Vote, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def create_movie(movie_id, title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(
        movie_id=movie_id, #integer
        title=title,  #string
        overview=overview,  #text
        release_date=release_date,  #string
        poster_path=poster_path,   #string
        #revenue=revenue,   #integer
        #video=video,   #boolean
        #runtime=runtime,   #integer
        #budget=budget,   #integer
    )

    return movie


def get_movies():
    """Return all movies."""

    return Movie.query.all()


def get_movie_by_id(movie_id):
    """Return a movie by primary key.""" 

    return Movie.query.get(movie_id)


def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)

    return rating


def update_rating(rating_id, new_score):
    """ Update a rating given rating_id and the updated score. """
    rating = Rating.query.get(rating_id)
    rating.score = new_score


def create_review(user, movie, title, review):
    """Create and return a new rating."""

    review = Review(user=user, movie=movie, review_title=title, user_review=review) 
    # the left side of the variable has to match the attributes in model.py Class Review

    return review


def update_review(review_id, new_review):
    """ Update a rating given rating_id and the updated score. """
    review = Review.query.get(review_id)
    review.review = new_review


def create_vote(user, movie, vote):
    """Create and return a new rating."""

    vote = Vote(user=user, movie=movie, vote=vote)

    return vote


def update_vote(vote_id, new_vote):
    """ Update a rating given rating_id and the updated score. """
    vote = Vote.query.get(vote_id)
    vote.vote = new_vote


if __name__ == "__main__":
    from server import app

    connect_to_db(app)