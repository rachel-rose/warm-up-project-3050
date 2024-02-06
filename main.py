from queries import Work


def main():
    q = Work()
    #q.load_data("warm-up-project-3050/movies-data.json") # User will give this as command line arg
    q.query("Movie Name", "==", "Rear Window")
    # THIS DOESNT WORK W CURRENT NAMING SYSTEM
    # WOULD HELP IF NAMES HAD NO SPACES


if __name__ == "__main__":
    main()
