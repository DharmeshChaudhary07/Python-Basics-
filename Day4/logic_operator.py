
##################################  Boolean expression ########################################

# # true false, function -> any() all() and many more.

# print(bool(True))
# print(bool(False))
# print(type(bool(True)))
# print(type(bool(False)))

# print(bool(123))
# print((bool("hello")))

# print((bool()))
# print((bool(0))) # outoput - false -> bool function it is considered as empty
# print((bool("")))

# print((bool(None))) # no value and no data types.

######################################## Functions ########################################

# # any(), all(), isinstance(), endswith(), startwith() ex. all function which return true or false/ bool,

# email = "sandy@gmail.com"
# phoneno = "+61 490213312"
# username = "zara"
# print(all([email, phoneno, username])) # goes as a list
# print(any([email, phoneno, username]))


email = "sandy@gmail.com"
phoneno = "+61 490213312"
username = ""
print(all([email, phoneno, username])) # goes as a list, returns false
print(any([email, phoneno, username]))

# print(isinstance(123, int))
# print(isinstance(True, str))
# print(isinstance(True, bool))

# email = "ayushi@gmail.com"
# print(email.endswith(".com"))
# print(email.startswith("ayu"))

