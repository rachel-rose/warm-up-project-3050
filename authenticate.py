import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred_path = "../warm-up-project-3050/warmup-project-61aa4-firebase-adminsdk-4d13y-72a1118150.json"


def db_connection():
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    return db
