
############################################################################################################################################################################################

# Operation we can do we list:

########################################################################################################################################################################


                                             # iterators and iterables (enumerate, reversed, zip, map)



# Any object capable of returning its members one at a time. To be an iterable, an object must implement the __iter__() method (which returns an iterator) or 
# the __getitem__() method.

# Iterator — "Remembers where it is" - An object that keeps track of its current position and produce next value while looping.
# __iter__(): Returns the iterator object itself
# __next__(): Returns the next item or raises a StopIteration error if no items remain.
# Simple rule: Every iterator is an iterable, but not every iterable is an iterator.

#                            iterable                       Iterator
# Can use in for loop.          ✅                             ✅
# Has __iter__()                ✅                             ✅
# Has __next__()                ❌                             ✅ 
# Reusable               ✅ multiple times.             ❌ one use only
# Examples.         list, tuple, str, dict, set.    map, zip, filter, reversed

# why do we need iterators: looping, save memory, speed flexibility

letter = ['a', 'b', 'c']
for l in letter:
    print(l)

for l in letter:
    print(l.upper())

newlist = []
for l in letter:
    # newlist += l.upper()
    newlist.append(l.upper())
    print(newlist)

####### iterator (enumerate, reversed, zip)  ##########

# enumerate - return index and value
# we can choose where to start from.

print(list(enumerate(letter)))  # prints <enumerate object at 0x1021b7100> iterator type at memory address
print(list(enumerate(letter)))  # prints [(0, 'a'), (1, 'b'), (2, 'c')]

print(list(enumerate(letter, start = 1)))    # [(1, 'a'), (2, 'b'), (3, 'c')]

for index, value in enumerate(letter):
    print(index, value)

print(list(reversed(letter)))   # returns an iterator that flips the data order.

for l in reversed(letter):
    print(l)

number = [1, 2, 3]
print(list(zip(letter, number)))

for l, n in zip(letter, number):     # combines two or more sequence into pair.
    print(l, n)

########## Map ###########

# map is fast, clean way to do data transformation.

letter = ['a', 'b', 'c']
print(map(str.upper, letter))
print(list(map(str.upper, letter)))

number = ['1', '2', '3']
print(list(map(int, number)))

name = ['rakhi ', '     deepak', ' mamta']
print(list(map(str.strip, name)))

for i in map(str.strip, name):
    print(i)

########################################################################################################################################################################


                                                 # filter (filter)

# filter( function, iterable)
                                        
letter = ['a', 'b','3', 'c', '7']
print(filter(str.isalpha, letter))      
print(list(filter(str.isalpha, letter)))                        

letter = ['a', 'b','', None, '7', 0, 'c', False]
print(list(filter(None, letter)))      # None removes all falsy value like 0, "" or false.
print(list(filter(bool, letter)))      # bool remove all falsy data same as None.

item = ['sql', '123', 'python', '42']
print(list(filter(str.isalpha, item)))      # ['sql', 'python']

for i in filter(str.isnumeric, item):     # prints 123
    print(i)                              #        42


########################################################################################################################################################################


                                                 # lambda

########## lambda #######
#  Syntax :- lambda arguments : expression
# eg. output = lambda x -> (input) : x + 2 -> (can be loop, check 'a' in X, methods, function , expression)
# use lambda for quick and custom logic.
# Rule: Lambda is just a shortcut for a simple function — anything lambda does, def can do too.
# mostly used with other data structure like map filter sorted.

multiply = lambda x : x * 2
print(multiply(5))

multiply =lambda x, y : x * y
print(multiply(3,5))
 
evenorodd =lambda x: "even" if x % 2 == 0 else "odd"
print(evenorodd(221))

check = lambda i : i in " python"
print(check('w'))

########## lambda + Map ###########

# Without map() — lambda only handles ONE item, Lambda doesn't know how to loop — it only works on one value at a time.

price = ['$340.23', '$345.30', '$234.30', '$453.40']
clean_price = list(map(lambda p : p.replace('$', ''), price))
print(clean_price)

# if price in float
clean_price = list(map(lambda p : float(p.replace('$', '')), price))
print(clean_price)

########## lambda + filter ###########

# remove all prices greater than 350
price = ['340', '355', '234', '453']
newprice = list(filter(lambda p : p > '350' , price))
print(newprice)

# keep only student with score higher than 70
student = [['makhi', 85],
           ['deepak', 80],
           ['max', 91]]
stud = list(filter(lambda row : row[1] > 90, student))
print(stud)

# task print student name starting with 'm'
stud = list(filter(lambda row : row[0].startswith('m'), student))
print(stud)

########## lambda + sort, sorted ############

student = [['makhi', 85],
           ['deepak', 80],
           ['max', 91]]

# sorted + lambda

# creates new sorted list original unchanged.
result = sorted(student, key=lambda s: s[1])
print(result)   
# [['deepak', 80], ['rakhi', 85], ['max', 91]]  ✅ original safe

# .sort() + lambda

# original is gone — no way to get it back
student.sort(key=lambda s: s[1])
print(student)   
[['deepak', 80], ['rakhi', 85], ['max', 91]]  # ✅ original changed

# .sort()   →  edits the original document  — old version gone
# sorted()  →  makes a photocopy and sorts it — original untouched


########################################################################################################################################################################


                                                 # List comprehension

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# syntax =[
#     #  data transformation 
#     #  loop
#     #  data filtering    (optional)
# ]



email = [ 'www.GOOGLE.com', 'localhost', 'www.OPENai.com', 'www.GMail.com']

mail = [
    i              # if no transformation need, add the loop variable : otherwise error
    for i in email
    if '.' in i
]
print(mail)

print(mail)
mail = [
    i.lower().replace('www.','')
    for i in email
    if '.' in i
]
print(mail)

# Note: i is just a loop variable — a nickname for each item. The real iterator is created by Python silently behind the scenes using iter().