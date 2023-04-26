"""Models for movie ratings app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    ratings = db.relationship("Rating", back_populates="user")
    reviews = db.relationship("Review", back_populates="user")
    votes = db.relationship("Vote", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"


class Movie(db.Model):
    """A movie."""

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)  # nullable is false because you don't want a movie without title
    overview = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    poster_path = db.Column(db.String)
    video = db.Column(db.Boolean)
    runtime = db.Column(db.Integer)
    budget = db.Column(db.Integer)
    revenue = db.Column(db.Integer)

    ratings = db.relationship("Rating", back_populates="movie")
    reviews = db.relationship("Review", back_populates="movie")


    def __repr__(self):
        return f"<Movie movie_id={self.movie_id} title={self.title}>"


class Rating(db.Model):
    """A movie rating."""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    popularity = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    score = db.Column(db.Integer)
   
    movie = db.relationship("Movie", back_populates="ratings")  # the back_populates need to match the variable in Class Movie, use "ratings"
    user = db.relationship("User", back_populates="ratings")    # the back_populates need to match the variable in Class User, use "ratings"

    def __repr__(self):
        return f"<Rating rating_id={self.rating_id}>"


class Review(db.Model):
    """A review."""

    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_review = db.Column(db.Text)
    review_title = db.Column(db.String)  # title is short, just use String
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    movie = db.relationship("Movie", back_populates="reviews")  # one movie has many reviews, back_populates should match variable in Class Movie, use "reviews"
    user =  db.relationship("User", back_populates="reviews")   # one user has many reviews, back_populates should match variable in Class User, use "reviews"
    votes = db.relationship("Vote", back_populates="review")    # One review has many votes, back_populates should match variable in Class Vote, use "review"

    def __repr__(self):
        return f"<Review review_id={self.review_id} score={self.user_review}>"
    

class Vote(db.Model):
    """A vote."""

    __tablename__ = "votes"
    
    vote_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    thumps_up = db.Column(db.Boolean)
    review_id = db.Column(db.Integer, db.ForeignKey("reviews.review_id"))    # One review can have many votes
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    review = db.relationship("Review", back_populates="votes")  # One review has many votes, back_populates should match varaible in Class Review, use "review"
    user = db.relationship("User", back_populates="votes")  # the back_populates need to match the variable in Class User

    def __repr__(self):
        return f"<Vote vote_id={self.vote_id} score={self.thumps_up}>"


def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=False): #database created, False because it will print out a lot of stuffs and become distracting.
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)