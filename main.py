from queries import Work


def main():
    q = Work()
    #q.load_data("warm-up-project-3050/movies-data.json") # User will give this as command line arg
    q.query("rating", "<", 7)
    #print("--------------DIVIDER!!!!!!!-------------")
    #q.or_query(["name", "director", "rating"], ["==", "==", "<"], ["Rear Window", "Alfred Hitchcock", 8.5])
    # THIS DOESNT WORK W CURRENT NAMING SYSTEM
    # WOULD HELP IF NAMES HAD NO SPACES


if __name__ == "__main__":
    main()
