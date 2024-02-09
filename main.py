from queries import Work


def main():
    q = Work()
    #q.load_data("warm-up-project-3050/movies-data.json") # User will give this as command line arg

    q.and_query([["year", "==", 2004.0]])
    print("______")
    q.and_query([["year", ">", 2000.0], ["rating", ">", 7.0]])
    print("______")
    # q.and_query([["year", ">", 2000.0], ["rating", ">", 7.0], ["director", "==", "Steven Spielberg"]])

    # print("--------------DIVIDER!!!!!!!-------------")
    # q.or_query([["name", "==", "Rocky"], ["rating", ">", 7.3], ["year", "==", 2004.0]])
    q.of_query(["name", "Rocky"])

if __name__ == "__main__":
    main()
