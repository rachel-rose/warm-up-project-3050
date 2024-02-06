from queries import Work

if __name__ == "__main__":
    filename = "warm-up-project-3050/movies-data.json" # User will give this as command line arg?

    work = Work()
    work.clear_data()
    work.load_data(filename)
