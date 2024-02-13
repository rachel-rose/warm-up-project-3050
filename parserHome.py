from pyparsing import Word, alphas, nums, alphanums, Literal, QuotedString
from authenticate import db_connection

# Global variable
keep_running = True

def parse_message(input_string):
    # Ways to compare values for a given token
    comparisons = Literal("==") | Literal("<=") | Literal(">=") | Literal("<") | Literal(">") | Literal("of")
    value = QuotedString('"') | Word('.' + nums)
    # Acceptible queries
    # example_query = Word(alphas) + comparisons + Word(alphanums + '"')
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
                print(type(results[2]))
                # Check if it is an 'of' query
                if(results[1] == "of"):
                    # Call the of query function
                    print("of query")
                else:
                    # Call query
                    print("success")
            else:
                # Throw exception
                print_help()

        # Compound query commands
        elif(query_size == 7):
            # Check if the token is valid at results[0], results[4]
            if(input_valid_token(results[0] and input_valid_token(results[4]))):
            
                # Check if the value field is numeric at results[2], results[6]
                results[2] = is_it_a_num(results[2])
                results[6] = is_it_a_num(results[6])

                # Check if it is an 'of' query
                if(results[1] == "of" or results[5] == "of"):
                    # Throw exception
                    print("No compound 'of' queries ")
                elif(results[3] == 'or'):
                    # Call 'or' query
                    print("or query")
                else:
                    # Call normal query
                    print("success")
            else:
                # Throw exception
                print_help()
        
        # Double compound query commands
        else:
            # Check if the token is valid at results[0], results[4], results[8]
            if(input_valid_token(results[0]) and input_valid_token(results[4] and input_valid_token(results[8]))):
               
                # Check if the value field is numeric at results[2], results[6], results[10]
                results[2] = is_it_a_num(results[2])
                results[6] = is_it_a_num(results[6])
                results[10] = is_it_a_num(results[10])

                # Check if it is an 'of' query
                if(results[1] == "of" or results[5] == "of" or results[9]):
                    # Throw exception
                    print("No compound 'of' queries ")
                elif(results[3] == 'or'):
                    # Call 'or' query
                    print("or query")
                else:
                    # Call normal query
                    print("success")
            else:
                # Throw exception
                print_help()
    except:
        #return error
        print_help()
    
def print_help():
    print("""************************************************\n************************************************\n\nTry using the following format: token comparison value \nFor example: year > 2020\nOr: name == "Rocky"
\nToken (category name): name, year, director, rating, genre, length, recommended, awards
Comparison: >, <, ==, >=, <=, of
Value:  “The Fast and the Furious”\n
Common formatting errors to avoid: 
\t- The \"of\" keyword should only be used proceding a specific movie name. ex: awards of \"movie name\" and cannot be a compound query\n
\t- You cannot put \"and\" and \"or\" in the same query\n
\t- Tokens (category names) should not be capitalized or in quotes 
\t- When searching by values (a specific movie name, genre, etc..), it must be in double quotation marks 
\t- Integers and floats do not have to be in quotation marks\n\n************************************************\n************************************************\n""") 

#make sure that when a number is put in, we convert it to a float
def is_it_a_num(input_str):
    if input_str.isdigit():
        input_str = float(input_str)
        return input_str
    else:
        return input_str

def input_valid_token(input_str):
    #tokens, comparisons, values
    token_list= ["year", "name", "director", "rating", "genre", "duration", "recommend", "awards"]
    for token in token_list:
        if input_str == token:
            return True
    return False

def main():
    # Call admin file with json file name
    db_connection()
    
    while(keep_running):
        user_query = input("Enter a query string in the format of 'token comparison value' ")
        parse_message(user_query)

main()
