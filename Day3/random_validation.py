
# ################################## Random ##################################
# # # random(), randint()

import random

# print(random.random()) 

# print(random.randint(11,56))

# ##### Use case --> use it to genrate test data( dummy) for like age., id, or prices


# ################################## Validation ##################################

# # # is_integer

# x = 7.0
# y = 7.1

# print(x.is_integer())
# print(y.is_integer())

# # # if the data is ending like this, a whole no but with two decimal point
# a = 44.00
# b = 12.000
# c = 144.00
# # # we check if numbers are truly whole floats (might just be from file export) 

# # # isintance(value, type) 
# x = 44
# y = 12.00
# print(isinstance(x, int))
# print(isinstance(x, float))
# print(isinstance(y, int))
# print(isinstance(y, float))


#################################### Challenge exerise #############################################

# print(random.randint(1,100) % 2)

number = random.randint(1,100)
is_even = bool(number % 2)
print(number)
print(is_even)
