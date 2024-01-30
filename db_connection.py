import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import requests
import json

cred_path = "../warm-up-project-3050/warmup-project-61aa4-firebase-adminsdk-4d13y-72a1118150.json"


def db_connection():
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    return db


url = "https://warmup-project-61aa4.firebaseio.com/movies-data.json"
jsondata = "../warm-up-project-3050/movies-data.json"
db = db_connection()
movies_ref = db.collection("Movies").document()

with open(jsondata, 'r') as inFile:
    data = json.load(inFile)

for movie in data:
    movies_ref.set(movie)




"""
class Movie:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
"""


#movies_ref.document("Whiplash").set(Movie("Whiplash", 4.5).to_dict())


#movies_ref.document("G-Force").set(Movie("G-Force", 1.2).to_dict())
