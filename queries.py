from google.cloud.firestore_v1.base_query import FieldFilter
from authenticate import db_connection
import json
import hashlib


class Movie:
    def __init__(self, name, year, director, rating, genre, recommend, duration, awards):
        self.name = name
        self.year = year
        self.director = director
        self.rating = rating
        self.genre = genre
        self.recommend = recommend
        self.duration = duration
        self.awards = awards

    # Turn data from dict to Movies object
    @staticmethod
    def from_dict(source):
        movie = Movie(source["name"], source["year"], source["director"], source["rating"], source["genre"], source["recommend"], source["duration"])

        if "awards" in source:
            movie.awards = source["awards"]
        else:
            movie.awards = None

        return movie

    def __repr__(self):
        return f"Movie:\nTitle = {self.name}\nYear = {self.year}\nDirector = {self.director}\nRating = {self.rating}\nGenre = {self.genre}\nRecommend = {self.recommend}\nDuration = {self.duration}\nAwards = {self.awards}"


# This is the class actually connected to the db
class Work:
    def __init__(self):
        self.db = db_connection()
        self.collection = self.db.collection("Movies")

    def load_data(self, filename):
        jsondata = "../" + filename

        # Create Movies collection
        movies_ref = self.collection

        # Load json data to firestore db
        with open(jsondata, 'r') as inFile:
            data = json.load(inFile)

        for movie in data:
            # print(movie)
            name = movie["Movie Name"].encode("utf-8")
            uuid = hashlib.shake_256(name).hexdigest(10)
            movies_ref.document(str(uuid)).set(movie)

    def clear_data(self):
        docs = (
            self.collection.list_documents()
        )

        for doc in docs:
            doc.delete()

    def update(self, id, key, value):
        self.collection.document(id).update({key: value})

    def query(self, token, comparison, value):
        # field_path = FieldPath([token])
        docs = (
                self.collection
                .where(filter=FieldFilter(token, comparison, value))
                .get()
        )
        if not docs:
            print(f"No movies with {token} {comparison} {value} :(")
        else:
            for doc in docs:
                doc_dict = doc.to_dict()
                print(doc_dict["id"])
                print(f"{doc_dict}")



