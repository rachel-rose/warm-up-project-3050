from pyparsing import Word, alphas, nums, alphanums, Literal, QuotedString
from queries import Work

# Global variables
keep_running = True
query_machine = Work()

# This parse_message method takes in an input string provided by the user and verifies if it matches
# a valid query in the defined query language. If it passes, the query is passed to the corresponding query
# method stored in queries.py.
def parse_message(input_string):
    # Ways to compare values for a given token
    comparisons = Literal("==") | Literal("<=") | Literal(">=") | Literal("<") | Literal(">") | Literal("of")

    # Acceptible values
    value = QuotedString('"') | Word('.' + nums)

    # Acceptible queries
    example_query = Word(alphas) + comparisons + value
    example_and_compound_query = Word(alphas) + comparisons + value + Literal("and") + Word(alphas) + comparisons + value
    example_or_compound_query = Word(alphas) + comparisons + value + Literal("or") + Word(alphas) + comparisons + value
    example_and_double_compound_query = example_and_compound_query + Literal("and") + Word(alphas) + comparisons + value
    example_or_double_compound_query = example_or_compound_query + Literal("or") + Word(alphas) + comparisons + value

    # Expected query format
    query = example_query ^ example_and_compound_query ^ example_or_compound_query ^ example_and_double_compound_query ^ example_or_double_compound_query ^ Literal("help") ^ Literal("quit")
    
    try:
        results = (query.parse_string(input_string, parse_all=True))
        query_size = len(results)

        # Single string commands
        if(query_size == 1):
            if(results[0] == "quit"):
                global keep_running 
                keep_running = False
            elif(results[0] == "help"):
                print_help()

        # Simply query commands
        elif(query_size == 3):
            # Check if the token is valid
            if(input_valid_token(results[0])):
                # Check if the value field is numeric
                results[2] = is_it_a_num(results[2])
                # Check if it is an 'of' query
                if(results[1] == "of"):
                    query_array = [results[0], results[2]]
                    # Call the 'of' query function
                    query_machine.of_query(query_array)
                else:
                    query_array = [[results[0], results[1], results[2]]]
                    # Call query
                    query_machine.and_query(query_array)
            else:
                # Invalid query
                print_help()

        # Compound query commands
        elif(query_size == 7):
            # Check if the token is valid at results[0], results[4]
            if(input_valid_token(results[0]) and input_valid_token(results[4])):            
                
                # Check if the value field is numeric at results[2], results[6]
                results[2] = is_it_a_num(results[2])
                results[6] = is_it_a_num(results[6])

                # Check if it is an 'of' query
                if(results[1] == "of" or results[5] == "of"):
                    # Invalid query
                    print("No compound 'of' queries. Type 'help' for more information.")
                elif(results[3] == 'or'):
                    query_array = [[results[0], results[1], results[2]], [results[4], results[5], results[6]]]
                    # Call 'or' query
                    query_machine.or_query(query_array)
                else:
                    query_array = [[results[0], results[1], results[2]], [results[4], results[5], results[6]]]
                    # Call standard query
                    query_machine.and_query(query_array)
            else:
                # Invalid query
                print_help()
        
        # Double compound query commands
        else:
            # Check if the token is valid at results[0], results[4], results[8]
            if(input_valid_token(results[0]) and input_valid_token(results[4]) and input_valid_token(results[8])):
               
                # Check if the value field is numeric at results[2], results[6], results[10]
                results[2] = is_it_a_num(results[2])
                results[6] = is_it_a_num(results[6])
                results[10] = is_it_a_num(results[10])

                # Check if it is an 'of' query
                if(results[1] == "of" or results[5] == "of" or results[9] == "of"):
                    # Invalid query
                    print("No compound 'of' queries. Type 'help' for more information.")
                elif(results[3] == 'or'):
                    query_array = [[results[0], results[1], results[2]], [results[4],results[5],results[6]], [results[8], results[9], results[10]]]
                    # Call 'or' query
                    query_machine.or_query(query_array)
                else:
                    query_array = [[results[0], results[1], results[2]], [results[4],results[5],results[6]], [results[8], results[9], results[10]]]
                    # Call standard query
                    query_machine.and_query(query_array)
            else:
                # Invalid query
                print_help()
    except:
        # Invalid query
        print_help()
    
# This print_help method displays the rules of the query language and gives examples on how 
# the user can query movies.
def print_help():
    print("""************************************************\n************************************************\n\nTry using the following format: token comparison value \nFor example: year > 2020\nOr: name == "Rocky"
\nToken (category name): name, year, director, rating, genre, length, recommended, awards
Comparison: >, <, ==, >=, <=, of
Value:  “The Fast and the Furious”\n
Common formatting errors to avoid: 
\t- The \"of\" keyword should only be used proceding a specific movie name. ex: awards of \"movie name\" and cannot be a compound query
\t- You cannot put \"and\" and \"or\" in the same query
\t- You cannot combine more than 3 queries with 'and' or 'or'
\t- Tokens (category names) should not be capitalized or in quotes 
\t- When searching by values (a specific movie name, genre, etc..), it must be in double quotation marks 
\t- Integers and floats do not have to be in quotation marks
          
When you are done type 'quit' to end the program\n\n************************************************\n************************************************\n""") 

# This is_it_a_num method takes in an input string and checks if it is numeric or a string.
# If it is numeric it is casted to a float and returned, else it is returned as is.
def is_it_a_num(input_str):
    is_num = True
    for i in input_str:
        if i.isalpha() :
            is_num= False
    if is_num == True:
        input_str = float(input_str)
    return input_str

# This input_valid_token method takes in an input string and compares it to each of the fields in the database.
# It returns true if it finds a match, else false.
def input_valid_token(input_str):
    #tokens, comparisons, values
    token_list= ["year", "name", "director", "rating", "genre", "duration", "recommend", "awards"]
    for token in token_list:
        if input_str == token:
            return True
    return False

# Our main welcomes the user to the database query interface and continually prompts for 
# queries until they enter 'quit'.
def main():
    # Welcome the user to the database
    print("Hello and welcome to our movies database query interface.")
    print("You can query the name, year, director, genre, rating, recommendation, duration or awards of your favorite movie!")
    print("Type 'help' for more information about queries")
    while(keep_running):
        user_query = input("Enter a query string in the format of 'token comparison value' ")
        parse_message(user_query)
    print("Thank you for using our database!")

main()
