from queries import Work


def main():
    q = Work()
    #q.load_data("warm-up-project-3050/movies-data.json") # User will give this as command line arg
    #q.query("year", "==", 1993.0)
    q.and_query([["awards", "==", 2000.0]])
    print("______")
    q.and_query([["year", ">", 2000.0], ["rating", ">", 7.0]])
    print("______")
    q.and_query([["year", ">", 2000.0], ["rating", ">", 7.0], ["director", "==", "Steven Spielberg"]])
    #print("--------------DIVIDER!!!!!!!-------------")
    #q.or_query(["name", "director", "rating"], ["==", "==", "<"], ["Rear Window", "Alfred Hitchcock", 8.5])
    # THIS DOESNT WORK W CURRENT NAMING SYSTEM
    # WOULD HELP IF NAMES HAD NO SPACES


if __name__ == "__main__":
    main()
