import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def db_connection():
    cred_path = "../pythonProject6/warmup-project-61aa4-firebase-adminsdk-4d13y-72a1118150.json"
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)
    db = firestore.client()


class Movie:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

movies_ref = db.collection("movies")
movies_ref.document("Whiplash").set(Movie("Whiplash", 4.5).to_dict())


movies_ref.document("G-Force").set(Movie("G-Force", 1.2).to_dict())
