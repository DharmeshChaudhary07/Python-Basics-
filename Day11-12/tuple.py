

########################################################################### Tuple ##############################################################################

# Quick Summary Table

# Operation                 List         Tuple    
# Change item                ✅             ❌
# append / insert            ✅             ❌
# remove / pop               ✅.            ❌
# sort / reverse in-place    ✅             ❌
# Use as dict key            ❌             ✅
# Faster & less memory       ❌             ✅


###############################################################################################################################################################





# Tuple 
# Tuples are used to store multiple items in a single variable
# A tuple is a collection which is ordered and unchangeable.

tuple = ("apple", "mango", "cherry")
print(tuple)

# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# we cannot change, add or remove items.
# order will not change.

tuple = ("apple", "mango", "cherry", "mango", "cherry")      # duplicate allowed
print(tuple)

tuple = ("apple", "banana", "cherry")
print(len(tuple))

tuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(tuple)

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 4, 2, 3)
tuple3 = (True, False, True)

print(tuple1)
print(tuple2)
print(tuple3)

########### Accessing tuple ############

# You can access tuple items by referring to the index number, inside square brackets:

tuple = ("apple", "banana", "cherry")
print(tuple[-1])

tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple[:4])

tuple = ("apple", "banana", "cherry")
if "banana" in tuple:
    print('banana')

########### Update tuple ############

# tuple are unchangeble but we can perform add/ remove and del by workaround :-
#### by converting it into a list then then again in tuple #####


########### unpacking tuple ############

tuple = ("apple", "banana", "cherry")
(red, yellow, blue) = tuple
print(tuple)
print(red)
print(yellow)
print(blue)

# using * asterisk 

tuple = ("apple", "banana", "mango", "papaya",  "cherry")
(red, *yellow, blue) = tuple
print(tuple)
print(red)          # <class 'str'>
print(yellow)       # <class 'list'>
print(blue)         # <class 'str'>


(red, *_ , blue) = tuple
print(tuple)
print(red)          # <class 'str'>
print(*_)           # individual str
print(blue)         # <class 'str'>

########### Looping in tuple ############(all works with list as well)
# using direct loop 

# using index loop (range and len)

tuple = ("mango" , "grapes", "banana")
for i in range(len(tuple)):
    print((tuple[i]))

list = ["mango" , "grapes", "banana"]

for i in range(len(list)):
    print(type(tuple[i]))

# or using enumerate()


for i, x in enumerate(tuple):   # tuple print with index no and value
    print(i, x)

for i, x in enumerate(list):    # list prints with index no and value
    print(i, x)

# while loop
i = 0 
while i < len(tuple):
    print(tuple[i])
    i += 1

########### join tuple ############

tuple1 = ("a", "b", "c", "a", "c" ,"c")
tuple2 = (1, 2, 3)
mewtuple = tuple1 + tuple2
print(mewtuple)
newtuple = tuple1 * 3
print(newtuple)

########### Tuple methods ############
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

tuplefinal = tuple1.count("c") 
print(tuplefinal)

tuplefinal1 = tuple1.index("b")
print(tuplefinal1)


