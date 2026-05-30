
################################ Comparison operator ########################################

# print(10 == 10)
# print(10 != 10)
# print(7 < 10)
# print(7 <= 10)
# print(7 > 10)
# print(7 >= 10)
# print(10 >= 10)

# # We can compare strings to alphabetically not just numbers

# print("a" < "b")
# print("abc" < "abb")
# print("abc" < "abd")
# print("a" < "A") # case sensative a and A treated as different value

# print("a" == "A") # = --> assigns, == --> compares
# print(7 < 10 < 9)
# print(7 < 10 < 12) # chain comparison left --> right , works like sql "between"- comparing two value in bound.

# age = 15
# print(11 <= age <= 22)

################################ Logical operator ########################################

# # # and, or, not
# print(3 > 1 and 3 > 2)
# print(3 > 1 and 3 < 2)
# print(3 < 1 and 3 < 2)

# print(3 > 1 or 3 > 2)
# print(3 > 1 or 3 < 2)
# print(3 < 1 or 3 < 2)

#### usecase ####

# #check if the system is under pressure/high usage

# cpu_usage = 70
# memory_usage = 90
# print(cpu_usage > 90 or memory_usage > 90) # atleast one is true then returns false

# # checking user credential before login
# email = True
# password = False
# print(email and password) # both should be true

# print(3 > 2)
# print( not 3 > 2) #we can put it before any boolean value to reverse the truth

# name = ""
# print(not name) 
# print(bool(0))
# print(not bool(0))

######## Practice question ########

# # allow access only if the user is logged in
# 3 or they are a guest
# but they must not be banned 

is_loggedin = True
is_guest = False
is_banned = False
print(is_loggedin or is_guest and not is_banned) #output ->true

is_loggedin = True
is_guest = False
is_banned = True
print(is_loggedin or is_guest and not is_banned) #output ->true 
# issue due to order of execution
is_loggedin = True
is_guest = False
is_banned = True
print((is_loggedin or is_guest) and not is_banned) #output ->false