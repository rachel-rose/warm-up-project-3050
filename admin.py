import sys
import json
from queries import Work

if __name__ == "__main__":
    # filename = "warm-up-project-3050/movies-data.json"  # User will give this as command line arg?
    filename = sys.argv[1]
    # update file for upload
    final_filename = "warm-up-project-3050/" + filename + ".json"

    # if else block for validation
    if final_filename != ' ':
        work = Work()
        work.clear_data()
        work.load_data(final_filename)
        print("File loaded successfully")

    else:
        print("File name not valid")



    #
    #
    # work = Work()
    # work.clear_data()
    # work.load_data(filename)
