import json
from authenticate import db_connection


def load_data():
    jsondata = "../warm-up-project-3050/movies-data.json"
    uuid = 0

    # Connect to database
    db = db_connection()

    # Create Movies collection
    movies_ref = db.collection("Movies")

    # Load json data to firestore db
    with open(jsondata, 'r') as inFile:
        data = json.load(inFile)

    for movie in data:
        uuid += 1
        movies_ref.document(str(uuid)).set(movie)
