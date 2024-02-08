import sys
from queries import Work

if __name__ == "__main__":
    while True:
        if len(sys.argv) < 2:
            print("ERROR! PLEASE ENTER JUST THE DATABASE NAME")
        else:
            filename = sys.argv[1]
            print(filename)


    # filename = "warm-up-project-3050/movies-data.json" # User will give this as command line arg?
    #
    # work = Work()
    # work.clear_data()
    # work.load_data(filename)
