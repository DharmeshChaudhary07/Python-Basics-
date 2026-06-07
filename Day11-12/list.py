 
############################################################## In-build Data Structure ###################################################################################



######################################################################################################
# Primitive and Non-Primitive Data Type

# Primitive     →  Single value  →  int, float, bool, string (string is consider primitive only in python)
# Non-Primitive →  Many values   →  list, tuple, set, dict

######################################################################################################

# Data structure
# It is a way of storing and organizing the data so, it can be used effciently 

# Built-in data structures (are predefined formats for organizing, storing, and manipulating data that are included as native features of a programming language).
# 1. list [10,20,40].  common 
# 2. tuple (10,30,20). No change
# 3. set {10,20,25}.   unique (no duplicate item)
# 4. dict. {10,20,20}. key : value

################################################################################ List ###############################################################################

# its just a ordered collection of item, changeable,allow duplicate (commonly used).
# stores the data in array unlike set uses hash function


# all the operation we can do we list
# how to create      # # how to access and read     # # how to unpack        # # how to explore and analyze  
# how to change      # # how to order               # # how to copy          # # how to combine  
# how to iterate     # # how to filter              # # how to tranform      # # list comprehension
 

########################################################################################################################################################################


                                             # Create list (two ways)

# Way 1

empty = []
letter = ['a', 'b', 'c']
number = [1,2,3]
print(empty)
print(type(empty))
print(letter)
print(type(letter[1]))
print(number)
print(type(number))
print(type(number[1]))

# we can mix datatype inside a list.
mixed =[1, "ayushi" , True, None , "a"]
print(mixed)
print(mixed[1])   # # index start from 0, prints ayushi

# Way 2

# build in function list() -> list(value) output: list
# coverts a iterable (sequence) into list

empty = list()
print(empty)
word = list("python")
print(word)
# number = list(range(5))
# print(number)

# nested list matrix  (Matrix = Data inside Data (nested) List  → most commonly used for matrix Tuple → works but immutable (can't change) NumPy → best for real matrix operations Set   → ❌ CANNOT make matrix  Dict  → ❌ CANNOT make matrix)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix)
print(type(matrix))

mixed_matrix = [[1,2,3],
                ['a','b'],
                [True]]
print(mixed_matrix)
print(type(mixed_matrix))

########################################################################################################################################################################

                                                # Access and read list

# acess and read list

# indexing  (only for 1 value)

list = ['a', 'b', 'c']
print(list)
print(list[2])    # print c  
print(list[-2])   # print b


# slicing  (for multiple value)

list = ['a', 'b', 'c', 'd']
print(list[1:3])     # print ['b', 'c']
print(list[1:4])     # print ['b', 'c', 'd']  index 4 so that it prints last item which has index 3
print(list[:])       # print ['a', 'b', 'c', 'd']
print(list[-2:-4])   # print [] why -> Python slicing by default moves LEFT → RIGHT. -2 to -4 means going backwards → so Python returns []


# access matrix list 

# indexing  (only for 1 value)

matrix = [[1,2,3],   # Row 0
          [4,5,6],   # Row 1
          [7,8,9]]   # Row 2
print(matrix[2])
print(matrix[2][2])
print(matrix[-1])
print(matrix[-1][-1])


# slicing  (for multiple value)

matrix = [[1,2,3],   # Row 0
          [4,5,6],   # Row 1
          [7,8,9]]   # Row 2
print(matrix[0:2])          # print [[1, 2, 3], [4, 5, 6]]
print(matrix[2][0:2])       # print [7, 8]
print(matrix[1][1:3])       # print [5, 6]

########################################################################################################################################################################

                                                            # Unpacking List

# unpacking the list (consist multiple items), taking out the item to store in the variable.
# use case 

person = ["Max", 30, "F1 driver", "Dutch"]
name = person[0]
age = person[1]
role = person[2]
country = person[3]

name, age, role, country = person      # order of variable should match order of value on list.
print(name)
print(role)



# rest collector Asterisk*

# create 3 variable, first item -> one variable, last item -> one variable , rest everything -> one variable.
# can use with two variable item on which we want to work -> one variable , and rest -> one variable.
# allowed to use only on asterisk at a time.

person = ["Max", 30, "F1 driver", "Dutch"]
name, *detail, country = person 
print(name)
print(detail)
print(country)

name, *detail = person 
print(name)
print(detail)

*detail, coutnry = person 
print(coutnry)
print(detail)



# rule of unpacking variable
# 1. no of variable must match the values exactly (if not using asterisk).
# 2. asterisk collect leftovers, and its fine if there are none.
# eg.
number = [1]
first, *leftover = number

print(first)       # print 1
print(leftover)    # print []

# 3. you can unpack any sequence (list, tuple, string)
# eg.
word = "Max"
first, *leftover = word
print(first)         # print M
print(leftover)      # print ['a', 'x']


# skipping items with underscore"_":

# allowed to use mutliple "_".
person = ["Max", 30, "F1 driver", "Dutch"]
name, _, _, country = person        # if not using few items in list, we can use _ 
print(name)
print(country)
print(_)         # print F1 driver (When _ is used twice, the second assignment overwrites the first)

# combining "_" and asterisk

person = ["Max", 30, "F1 driver", "Dutch"]
name, *_, country = person        # if not using few items in list, we can use _ 
print(name)
print(country)
print(_)   

########################################################################################################################################################################

                                                            # Explore and Analyze

# Use multiple function:

# max(), min(), sum(), len()                           -> analyze     (functions)
# all(), any()                                         -> completeness and existence checker (returns true or false)
# .count, .index                                       -> search and count    (method)
# 'a' in 'a','b' (true) , 'a' is 'a','b'(false)        -> membership and identity   (operator)
# 'a','b' == a','b' (true), 'a','b' > a','b' (false)   -> comparsion

number= [102,204,305,401,500,204,345,204]
print("max:", max(number))
print("min:", min(number))
print("sum:", sum(number))
print("length:", len(number))

print("All:", all(number))      # return true if all the items are true
print("All:", all([204,305,401]))
print("All:", all([204,454,401]))    # return true ( all() has nothing to do with your number list! It only checks if every element is truthy or falsy )
print("All:", all([204,0,401]))     # false
print("All:", all([204,"",401]))    # false
print("All:", all(['a','b','c']))   # true

print("Any:", any(number))      # return true if any the items are true
print("Any:", any([204,0,401])) 
print("Any:", any(['a', '', 'b'])) 
print("Any:", any([0, 0, 0]))   # only time it will be false

print("Count:", number.count(204)) 

# .index -> returns the position of the first occurrence of a value
print("Index:", number.index(204))
print("Index:", number.index(345))

print(204 in number)
print(204 not in number)

list1 = [1,2,3]
list2 = [1,2,3]
print(list1 == list2)   # print true
list3 = [1,2,3,4]
print(list1 > list2)

print(list1 is list2)   # false (is operator check if it stored in same memory address) here list1 and list2 are identical but stored at differnet memory address


#################################################################################################################################################################