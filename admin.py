import sys
from queries import Work

if __name__ == "__main__":
        #
    if len(sys.argv) < 2 or len(sys.argv) >= 3:
        print("ERROR! PLEASE ENTER JUST THE DATABASE NAME AND THE PYTHON FILE")
    else:
        filename = sys.argv[1]
        update_filename = "warm-up-project-3050/" + filename +".json"
        work = Work()
        work.clear_data()
        work.load_data(update_filename)
        print("File loaded successfully")



    # filename = "warm-up-project-3050/movies-data.json" # User will give this as command line arg?
    #
    # work = Work()
    # work.clear_data()
    # work.load_data(filename)
