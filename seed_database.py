"""Script to seed database."""
import crud
import os
import requests
import json
from random import choice, randint
from datetime import datetime

import model
import server


# get json data from TMBD
url = "https://api.themoviedb.org/3/search/movie?api_key=c4460360e6e1738f734e1ed2ea4ef0e3&query=Star+Trek"
response = requests.get(url)
os.system("dropdb ratings")
os.system("createdb ratings")


model.connect_to_db(server.app)
model.db.create_all()

movie_data = response.json() #convert it to the dict
#print(movie_data)
#print(type(movie_data))
#print(movie_data.keys())

# Create movies, store them in list so we can use them
# to create fake ratings
movies_in_db = []
for movie in movie_data["results"]:  # if I don't use result, I will get a dict that I can't loop through that
    movie_id, title, overview, poster_path, backdrop_path = (
        movie["id"],
        movie["title"],
        movie["overview"],
        movie["poster_path"],
        movie["backdrop_path"],
        #movie["runtime"],
        #movie["budget"],
        #movie["revenue"],
    )
    
    notMovie_id = [282759, 332626, 26965, 1111972, 161334]
    
    if movie_id not in notMovie_id:
        release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")
        db_movie = crud.create_movie(movie_id, title, overview, release_date, poster_path, backdrop_path)
        movies_in_db.append(db_movie)

model.db.session.add_all(movies_in_db)
model.db.session.commit()


# Create 10 users; each user will make 10 ratings
for n in range(1, 10):
    email = f"user{n}@test.com"  # Create unique email
    password = "test"

    user = crud.create_user(email, password)
    model.db.session.add(user)

    for _ in range(1, 10):   # _ doesn't care about what the iterator value is
        random_movie = choice(movies_in_db) 
        score = randint(1, 5)

        rating = crud.create_rating(user, random_movie, score)
        model.db.session.add(rating)

model.db.session.commit()
