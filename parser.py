from pyparsing import Word, alphas, nums, alphanums, Literal, QuotedString
from authenticate import db_connection

# Global variable
keep_running = True

def parse_message(input_string):
    # Ways to compare values for a given token
    comparisons = Literal("==") | Literal("<=") | Literal(">=") | Literal("<") | Literal(">") | Literal("of")
    value = QuotedString('"') | Word(nums)
    # Acceptible queries
    # example_query = Word(alphas) + comparisons + Word(alphanums + '"')
    example_query = Word(alphas) + comparisons + value
    example_and_compound_query = Word(alphas) + comparisons + Word(alphanums + '"') + Literal("and") + Word(alphas) + comparisons + Word(alphanums + '"')
    example_or_compound_query = Word(alphas) + comparisons + Word(alphanums + '"') + Literal("or") + Word(alphas) + comparisons + Word(alphanums + '"')
    example_and_double_compound_query = example_and_compound_query + Literal("and") + Word(alphas) + comparisons + Word(alphanums + '"')
    example_or_double_compound_query = example_or_compound_query + Literal("or") + Word(alphas) + comparisons + Word(alphanums + '"')

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
            # TODO: Call input_valid_token function

            # Check if the value field is numeric
            # TODO: Call is it a number

            # Check if it is an 'of' query
            if(results[1] == "of"):
                # Call the of query function
                print("of query")
            else:
                print("success")

        # Compound query commands
        elif(query_size == 7):
            # Check if the token is valid at results[0], results[4]
            # TODO: Call input_valid_token function
            
            # Check if the value field is numeric at results[2], results[6]
            # TODO: Call is it a number

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
        
        # Double compound query commands
        else:
            # Check if the token is valid at results[0], results[4], results[9]
            # TODO: Call input_valid_token function
            
            # Check if the value field is numeric at results[2], results[6], results[11]
            # TODO: Call is it a number

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
    except:
        #return error
        print_help()
    
def print_help():
    print("""************************************************\n************************************************\n\nTry using the following format: token comparison value \nFor example: year > 2020\nOr: name == "Rocky"
\nToken (category name): name, year, director, rating, genre, length, recommended, awards
Comparison: >, <, ==, >=, <=, of
Value:  “The Fast and the Furious”\n
Common formatting errors to avoid: 
\t- Tokens (catergory names) should not be capialized or in quotes 
\t- When searching by values (a specific movie name, genre, etc..), it must be in double quotation marks 
\t- Integers and floats do not have to be in quotation marks\n\n************************************************\n************************************************\n""") 

def main():
    # Call admin file with json file name
    db_connection()
    
    while(keep_running):
        user_query = input("Enter a query string in the format of 'token comparison value' ")
        parse_message(user_query)

main()