from queries import Work


def main():
    q = Work()
    #q.load_data("warm-up-project-3050/movies-data.json") # User will give this as command line arg

    q.and_query([["rating", "==", "No"]])
    print("______")
    #q.or_query([["name", "==", "dogs"], ["year", "==", "dogs"]])
    print("______")
    # q.and_query([["year", ">", 2000.0], ["rating", ">", 7.0], ["director", "==", "Steven Spielberg"]])

    # print("--------------DIVIDER!!!!!!!-------------")
    # q.or_query([["name", "==", "Rocky"], ["rating", ">", 7.3], ["year", "==", 2004.0]])
    #q.of_query(["year", "Rocky"])


if __name__ == "__main__":
    main()
