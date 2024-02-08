from pyparsing import Word, alphas, nums, one_of, Optional, alphanums

greet = Word(alphas) + "," + Word(alphas) + "!"

user_query = input("Enter a query string in the format of 'token comparison value' ")
hello = "Hello, World!"
print(hello, "->", greet.parse_string(hello))
# query = Word(alphas) + Word(one_of) + Word(alphas)
query_test = "token == value"
# print(query_test, "->", query2.parse_string(query_test))
# example_query = "genre == horror"
# print(example_query, "->", query.parse_string(example_query))
comparisons = ["and", "or", "of", "==", "<", ">", "<=", ">="]
# comparison = Word(alphas)["=="]
# query3 = Word(alphas) + comparison + Word(alphas)
# print(query_test, "->", query3.parse_string(query_test))
query = Word(alphas) + Word("and" + "or" + "of" + "==" + "<" + ">" + "<=" + ">=") + Word(alphanums + '"') + Optional(Word(alphas)) + Optional(Word(alphanums)) + Optional(Word("and" + "or" + "of" + "==" + "<" + ">" + "<=" + ">=")) + Optional(Word(alphanums))
print(query_test, "->", query.parse_string(query_test))


#query_test_2 = "token == value and token2 <= value2"
results = (user_query, "->", query.parse_string(user_query))
for result in results:
    print(result)

print("*&*******")
count = 0
tokens = []
comparisons = []
values = []
for value in results[2]:
    if(count % 4 == 0):
        tokens.append(results[2][count])
    elif(count % 4 == 1):
        comparisons.append(results[2][count])
    elif(count % 4 == 2):
        # If string with quotes
        if(value.isdigit() == False):
            value_string = results[2][count][1:-1]
            values.append(value_string)
        else:
            values.append(results[2][count])
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