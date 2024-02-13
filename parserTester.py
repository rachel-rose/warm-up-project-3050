from pyparsing import Word, alphas, nums, one_of, Optional, alphanums, QuotedString, Group

example_query = Word(alphas) + Word("of" + "==" + "<" + ">" + "<=" + ">=") + Word(alphanums + '"')
#example_query = Word(alphas) + Word("of" + "==" + "<" + ">" + "<=" + ">=") + Word(alphanums + '"') ^ Word(alphas) + Word(alphas) + Word("of" + "==" + "<" + ">" + "<=" + ">=") + Word(alphanums + '"') ^ Word(alphas) + Word(alphas) + Word("of" + "==" + "<" + ">" + "<=" + ">=") + Word(alphanums + '"') + Word(alphas) + Word(alphas) + Word("of" + "==" + "<" + ">" + "<=" + ">=") + Word(alphanums + '"') 

example_compound_query = Word(alphas) + Word("of" + "==" + "<" + ">" + "<=" + ">=") + Word(alphanums + '"') + Word(alphas) + Word(alphas) + Word("of" + "==" + "<" + ">" + "<=" + ">=") + Word(alphanums + '"')

#query = example_query + Optional(example_compound_query)  
query = example_query ^ example_compound_query 
greet = Word(alphas) + "," + Word(alphas) + "!"

try:

    user_query = input("Enter a query string in the format of 'token comparison value' ")
    hello = "Hello, World!"
    #print(hello, "->", greet.parse_string(hello))
    # query = Word(alphas) + Word(one_of) + Word(alphas)
    query_test = "token == value"
    # print(query_test, "->", query2.parse_string(query_test))
    # example_query = "genre == horror"
    # print(example_query, "->", query.parse_string(example_query))
    comparisons = ["and", "or", "of", "==", "<", ">", "<=", ">="]
    # comparison = Word(alphas)["=="]
    # query3 = Word(alphas) + comparison + Word(alphas)
    # print(query_test, "->", query3.parse_string(query_test))
    #query = Word(alphas) + Word("of" + "==" + "<" + ">" + "<=" + ">=") + Word(alphanums + '"') + Optional(Optional(Word(alphas)) + Optional(Word(alphanums)) + Optional(Word("of" + "==" + "<" + ">" + "<=" + ">=")) + Optional(Word(alphanums + '"')))
    #print(query_test, "->", query.parse_string(query_test))


    #query_test_2 = "token == value and token2 <= value2"
    results = (query.parse_string(user_query))
    for result in results:
        print(result)


    # def get_input():
    #     valid_input = False
    #     while(not valid_input):
    #         user_query = input("Enter a query string in the format of 'token comparison value' : ")
    #         word_count = 0
    #         user_query = user_query.split()
    #         word_count = len(user_query)

    #         if(word_count % 3 == 0)
    #         {
    #             # call 1 query parsing
    #         }






    print("*&*******")
    count = 0
    tokens = []
    comparisons = []
    values = []
    for value in results:
        if(count % 4 == 0):
            tokens.append(results[count])
        elif(count % 4 == 1):
            comparisons.append(results[count])
        elif(count % 4 == 2):
            # If string with quotes
            if(value.isdigit() == False):
                #value_string = results[count][1:-1]
                values.append(value_string)
            else:
                values.append(results[count])
            # Else
            # values.append(results[2][count])
        # The value is an "and" or "or" if it reaches this point without going into an if statement.
        count += 1

    token_string = "List Parameter 1: "
    for token in tokens:
        token_string += token + " "
    comparison_string = "List Parameter 2: "
    for comparison in comparisons:
        comparison_string += comparison + " "
    value_string = "List Parameter 3: "
    for value in values:
        value_string += value + " "
    print(token_string)
    print(comparison_string)
    print(value_string)

except:
    print("There was an error in your input. Here are some examples to follow:"
          "Tokens (catergory names) should not be capialized or in quotes"
          "Values must be in double quotation marks"
          "Integers and floats should not be in quotation marks"
          "The \"of\" key word should only be used proceding a specific movie name. ex: awards of \"movie name\"")

 #MY STUFFF

def format_for_query():
    #what do i do if there are multiple items
    #2d list
    new_array= []
    #tokens, comparisons, values
    for token in tokens:
        new_array.append(token)
    for comparison in comparisons:
        new_array.append(comparison)
    for value in values:
        new_array.append(value)
    return new_array

#input validation
#make sure that when a number is put in, we convert it to a float
def is_it_a_num(input_str):
    if input_str.isdigit():
        input_str = float(input_str)
        return input_str

# check if user input their query correctly
# if not throw an error and tell them to fix it

# Tokens (catergory names) should not be capialized or in quotes
# Values must be in double quotation marks
# Integers and floats do not have to be in quotation marks
def input_valid_token(tokens):
    #tokens, comparisons, values
    if token[0].isupper():
        print("is quote")
        #throw exception

input_valid(tokens)

#try block, if throws an error, then catch will wrot our error
#try:
    # put everything in here

# you need to sense or and of
# if "or" in query pass to or_query() function
#elif "of" in query pass to of_query() function
#else and_query()

def sense_compound():
    compounds = ["and", "or", "of"]

#fromQueryinport, theyre in a class, make an object


#help and quit function
#calll help when we reach an except statmnt
