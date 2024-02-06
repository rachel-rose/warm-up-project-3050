from pyparsing import Word, alphas, nums, one_of

greet = Word(alphas) + "," + Word(alphas) + "!"

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
query = Word(alphas) + Word("and" + "or" + "of" + "==" + "<" + ">" + "<=" + ">=") + Word(alphas)
print(query_test, "->", query.parse_string(query_test))
