"""Server for movie ratings app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db, Rating, Review
import crud
import requests
import json
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")


@app.route("/movies")
def all_movies():
    """View all movies."""

    movies = crud.get_movies()

    return render_template("all_movies.html", movies=movies)


@app.route("/movies/<movie_id>")
def show_movie(movie_id):
    """Show details on a particular movie."""
    
    movie = crud.get_movie_by_id(movie_id)
  
    # make an API call
    base_url = 'https://api.themoviedb.org/3/movie/'
    APIkey = '/videos?api_key=c4460360e6e1738f734e1ed2ea4ef0e3'
    APIlink = base_url + movie_id + APIkey
    
    print(APIlink)

    # get video info
    response = requests.get(APIlink)
    video_data = response.json()
    print(video_data['results'][0])
    key = video_data['results'][0]['key']

    link = "https://www.youtube.com/watch?v=" + key

    return render_template("movie_details.html", movie=movie, link=link)


@app.route("/users")  # first display the page
def all_users():    
    """View all users."""
    users = crud.get_users()

    return render_template("all_users.html", users=users)


@app.route('/searchResult.text', methods=["POST"]) #remember to put method
def search_display():
    """Search the email and display all the movies and ratings by this email"""
    email = request.json.get('email')

    user = crud.get_user_by_email(email)

    if not user:    
        flash("Can't find emails! Please search again!") 
        sendDict = {}  #return it to bottom, if you get user in the db, sendDict will be undefined and will be an error
    else:
        result_code = "OK"
        result_text = f"You got search results!"
        sendDict = {'user_id': user.user_id,
                   'email': user.email,
                   }

    return sendDict


@app.route("/users/<user_id>")
def show_user(user_id):
    """Show details on a particular user."""

    user = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user)


@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")


@app.route("/login", methods=["POST"])
def process_login(): 
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}!")

    return redirect('/')


@app.route("/login2/<movie_id>", methods=["POST"])
def process_login2(movie_id):
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}!")

    return redirect(f'/movies/{movie_id}')


@app.route("/logout")
def process_logout():
    session.pop('user_email', None)
    flash('You were logged out.')
    
    return redirect('/')


"""SHOULD I PASS movie_id INTO THIS DEFINITION? """
"""SHOULD I ALSO PASS IN THE user_id INTO THIS DEFINITION? """
@app.route("/update_rating", methods=["POST"])
def update_rating():
    rating_id = request.json["rating_id"] #rating_id from .js
    updated_score = request.json["updated_score"] #updated_rating from .js
    Rating.update(rating_id, updated_score)
    #crud.update_rating(rating_id, updated_score)
    db.session.commit()
    
    flash(f"You have updated this movie ratings to {updated_score} out of 5!")  #THIS DOESN"T WORK!!!
    
    return "Success"


@app.route("/update_review", methods=["POST"])
def update_review():
    review_id = request.json["review_id"]
    updated_review = request.json["updated_review"]
    Review.update(review_id, updated_review)
    db.session.commit()
    
    flash(f"You have updated this movie!")  #THIS DOESN"T WORK!!!
    
    return "Success"


@app.route("/movies/<movie_id>/ratings", methods=["POST"])
def create_rating(movie_id):
    """Create a new rating for the movie."""

    logged_in_email = session.get("user_email")
    rating_score = request.form.get("rating")

    if logged_in_email is None:
        flash("You must log in to rate a movie.")
    elif not rating_score:
        flash("Error: you didn't select a score for your rating.")
    else:
        user = crud.get_user_by_email(logged_in_email)
        movie = crud.get_movie_by_id(movie_id)

        rating = crud.create_rating(user, movie, int(rating_score))
        db.session.add(rating)
        db.session.commit()

        flash(f"You rated this movie {rating_score} out of 5.")

    return redirect(f"/movies/{movie_id}")


@app.route("/movies/<movie_id>/review", methods=['POST'])  # review
def create_review(movie_id):

    logged_in_email = session.get("user_email")
    review_title = request.form.get("review_title")
    user_review = request.form.get("user_review")

    if logged_in_email is None:
        flash("You must log in to write a review.")
    elif not user_review:
        flash("Error: Review is missing.")
    elif not review_title:
        flash("Error: Review Title is missing.")
    else:
        user = crud.get_user_by_email(logged_in_email)
        movie = crud.get_movie_by_id(movie_id)

        review = crud.create_review(user, movie, review_title, user_review)
        db.session.add(review)
        db.session.commit()
    
        flash(f"You wrote a review of {movie.title}.")

    return redirect(f"/movies/{movie_id}")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
