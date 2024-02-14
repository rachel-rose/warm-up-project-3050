from google.cloud.firestore_v1.base_query import FieldFilter
from authenticate import db_connection
import json
import hashlib

class Movie:
    # Initializes a Movie object with the given parameters
    def __init__(self, name, year, director, rating, genre, recommend, duration, awards):
        self.name = name
        self.year = year
        self.director = director
        self.rating = rating
        self.genre = genre
        self.recommend = recommend
        self.duration = duration
        self.awards = awards

    # Converts dictionary to Movie object
    @staticmethod
    def from_dict(source):
        movie = Movie(source["name"], source["year"], source["director"], source["rating"], source["genre"], source["recommend"], source["duration"])
        if "awards" in source:
            movie.awards = source["awards"]
        else:
            movie.awards = None

        return movie

    # Returns a string representation of a Movie object
    def __repr__(self):
        return f"Movie:\nTitle = {self.name}\nYear = {self.year}\nDirector = {self.director}\nRating = {self.rating}\nGenre = {self.genre}\nRecommend = {self.recommend}\nDuration = {self.duration}\nAwards = {self.awards}"


# This is the class actually connected to the db
class Work:
    # Initializes a Work object and starts database connection to the Movies collection
    def __init__(self):
        self.db = db_connection()
        self.collection = self.db.collection("Movies")

    # Converts a dictionary to a Movie object
    @staticmethod
    def to_movie(source):
        return Movie.from_dict(source)

    # Takes in a json file and loads the given data into a Google Cloud Firestore database
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

    # Deletes all data from the Movies collection
    def clear_data(self):
        docs = (
            self.collection.list_documents()
        )

        for doc in docs:
            doc.delete()

    # Takes in the ID of a document and a key:value pair then updates the given
    # key in that document with the given value
    def update(self, id, key, value):
        self.collection.document(id).update({key: value})

    # This is a helper function for the other query functions. It takes in a token (key)
    # a comparison operator, and a value, then searches the collection for all documents
    # with the given requirements and returns a subcollection of documents
    def query(self, token, comparison, value):
        docs = (
                self.collection
                .where(filter=FieldFilter(token, comparison, value))
                .get()
        )
        return docs

    # The or_query function takes in a list of up to three token, comparison, value groups and
    # prints each document that satisfies ANY of the given requirements
    def or_query(self, list):
        for i in range(len(list)):
            docs = self.query(list[i][0], list[i][1], list[i][2])
            if not docs:
                output = "Sorry, no movies found with "
                #for i in range(len(list)):
                    #output += item[0] + " " + item[1] + " " + item[2]
                    #if
                    #output += " or "
                print(output)
            else:
                for doc in docs:
                    # Remove duplicate documents
                    docs.remove(doc)
                    doc_dict = doc.to_dict()

                    # print(doc_dict["id"])
                    print(f"{doc_dict}")

    # The and_query function takes in a list of up to three token, comparison, value groups and
    # prints each document that satisfies ALL of the given requirements
    def and_query(self, list):
        # One query given
        if (len(list)) == 1:
            docs = self.query(list[0][0], list[0][1], list[0][2])
            self.print_docs(docs)

        # Two queries given
        elif (len(list)) == 2:
            docs = self.query(list[0][0], list[0][1], list[0][2])
            docs2 = self.query(list[1][0], list[1][1], list[1][2])

            final = []
            for doc in docs:
                if doc in docs2:
                    final.append(doc)

            self.print_docs(final)

        # Three (max) queries given
        else:
            docs = self.query(list[0][0], list[0][1], list[0][2])
            docs2 = self.query(list[1][0], list[1][1], list[1][2])
            docs3 = self.query(list[2][0], list[2][1], list[2][2])

            final = []
            for doc in docs:
                if doc in docs2 and doc in docs3:
                    final.append(doc)

            self.print_docs(final)

    # The of_query function takes in a list with two items: attribute and movie title
    # The function finds the movie with the given title then prints the desired attribute
    def of_query(self, list):
        attribute = list[0]
        title = list[1]

        # Get desired movie and convert to dictionary
        docs = (
            self.collection
            .where(filter=FieldFilter("name", "==", title))
            .get()
        )
        for doc in docs:
            doc_dict = doc.to_dict()

        # If attribute found, print to console
        final = []
        if doc_dict[attribute] != "":
            final.append(doc_dict[attribute])
            print(final[0])
        else:
            print(f"The movie", title, "has no", attribute)

    # Takes in a collection of documents and prints them to the console
    def print_docs(self, docs):
        if not docs:
            print("Sorry, no movies found.")
        for doc in docs:
            doc_dict = self.format_dict(doc.to_dict())
            print(f"{doc_dict}")

    # Takes in a dictionary and returns it as a formatted string
    def format_dict(self, source):
        mystr = ("Title: " + source["name"] + ", Director: " + source["director"] + ", Year: " + str(source["year"])
                 + ", Rating: " + str(source["rating"]) + ", Genre: " + source["genre"] + ", Duration: "
                 + str(source["duration"]) + ", Recommend: " + str((source["recommend"])))

        if source["awards"] != "":
            mystr += ", Awards: " + source["awards"]

        return mystr


    # function that checks if certain tokens are being passed in with strings
    # tokens that don't accept strings: rating, duration, year
    # example rating == "8.2" return a bad output
    def check_token(self, list):
        for i in range(len(list)):
            if list[i][0] == 'year' or 'rating' or ' duration':
                if isinstance(list[i][2], str):
                    # return bool
                    return False
        return True