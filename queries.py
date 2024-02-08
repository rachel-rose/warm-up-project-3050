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

    @staticmethod
    def to_movie(source):
        return Movie.from_dict(source)

    def load_data(self, filename):
        jsondata = "../" + filename

        # Create Movies collection
        movies_ref = self.collection

        # Load json data to firestore db
        with open(jsondata, 'r') as inFile:
            data = json.load(inFile)

        for movie in data:
            # print(movie)
            name = movie["name"].encode("utf-8")
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
        return docs

    def or_query(self, list):
        for i in range(len(list)):
            docs = self.query(list[i][0], list[i][1], list[i][2])

            if not docs:
                print(f"No movies with xyz :(")
            else:
                for doc in docs:
                    docs.remove(doc)
                    doc_dict = doc.to_dict()

                    # print(doc_dict["id"])
                    print(f"{doc_dict}")

    def and_query(self, list):
        if (len(list)) == 1:
            self.query(list[0][0], list[0][1], list[0][2])

        elif (len(list)) == 2:
            docs = self.query(list[0][0], list[0][1], list[0][2])
            docs2 = self.query(list[1][0], list[1][1], list[1][2])

            final = []

            for doc in docs:
                if doc in docs2:
                    final.append(doc)

            self.print_docs(final)

        else:
            docs = self.query(list[0][0], list[0][1], list[0][2])
            docs2 = self.query(list[1][0], list[1][1], list[1][2])
            docs3 = self.query(list[2][0], list[2][1], list[2][2])

            final = []
            for doc in docs:
                if doc in docs2 and doc in docs3:
                    final.append(doc)

            self.print_docs(final)

    # of query
    # user types in "Awards OF title name"
    # Not given the option to type anything other than film name
    # takes in list like so ['token','comparison', 'field']
    def of_query(self, list):
        # vars
        name = list[0]
        comp = list[1]
        title = list[2]
        # query for movie
        docs = (
            self.collection
            .where(filter=FieldFilter(name, comp, title))
            .get()
        )
        for doc in docs:
            doc_dict = doc.to_dict()
        # check if movie has an awards and
        # print corresponding statement
        final = []
        if doc_dict["awards"] != "":
            final.append(doc_dict["awards"])
            print(final)
        else:
            print(f"The movie", title, "has no awards.")



    # if not docs:
    #     print(f"No awards for the movie: ", list[0])
    # else:
    #     self.print_docs(docs)


    def print_docs(self, docs):
        if not docs:
            print("Sorry, there are no movies with ")
        for doc in docs:
            #docs.remove(doc)
            doc_dict = self.format_dict(doc.to_dict())
            print(f"{doc_dict}")

    def format_dict(self, source):
        mystr = ("Title: " + source["name"] + ", Director: " + source["director"] + ", Year: " + str(source["year"])
                 + ", Rating: " + str(source["rating"]) + ", Genre: " + source["genre"] + ", Duration: "
                 + str(source["duration"]) + ", Recommend: ")
        if source["recommend"]:
            mystr += "Yes"
        else:
            mystr += "No"

        if "awards" in source:
            mystr += ", Awards: " + source["awards"]

        return mystr

