

############################################################### dictionaries ########################################################

# dict 
# stores different value to one variable. like customer = name,age,country (to one variable customer)
# syntax -
# coustmer = { keys(description of data) : value (data) }
# eg. coustmer = { name : alex, age : 33, country : japan}

my_dict = {
    'a' : 10,
    'b' : 20,
    'c' : 30,
    }

print(my_dict)                # ordered

# keys are unique and value allows duplicate
my_dict = {
    'a' : 10,
    'b' : 20,
    'c' : 30,
    'a' : 10                    # if d instead -  prints {'a': 10, 'b': 20, 'c': 30, 'd': 10} 
    }
print(my_dict)                  # prints {'a': 10, 'b': 20, 'c': 30}

print(my_dict[1])               # dict - no indexing 
print(my_dict['b'])             # but value can be accessed by their keys.

# mutable
my_dict['c'] = 50               # mutable
print(my_dict)


####### dict method ########

user = {'id' : 112, 'age' : 33, 'city' : 'sydney'}
print(user)

# access
print(user['id'])                    # prints 112
print(user['names'])                # prints error, instead use .get() to get none if doesnt exist instead of error.

# .get() - returns the value safely, give None if missing key.
print(user.get('name'))               # prints none
print(user.get('name', "unknown"))    # prints unknown



####### checks in dict ########
# in operator - checks if the key is inside the dict
print('city' in user)
print('name' not in user)


########### view objects ############
# give you a live view of the dict keys, value or key value pair.
# .items() perfect when oyu need key and value togther for looping transforming data, building new dicts, comparing and more.
# they creates it into a tuple.

print(user.keys())                      # prints dict_keys(['id', 'age', 'city'])
print(user.values())                    # dict_values([112, 33, 'sydney'])
print(user.items())                     # dict_items([('id', 112), ('age', 33), ('city', 'sydney')])


######### Looping ########

# 
for u in user:
    print(u, user[u])

# instead use better way
for key, value in user.items():
    print(key, value)


######### add remove and update ########

user['name'] = 'john' 
print(user)                             # prints {'id': 112, 'age': 33, 'city': 'sydney', 'name': 'john'} -> adds name and value

user["age"] = 35                          # prints {'id': 112, 'age': 35, 'city': 'sydney'} -> update age
print(user)
user.update({'age' : 40, "city": "melbourne"})
print(user)                               # prints {'id': 112, 'age': 40, 'city': 'melbourne'} - update multiple value at once


user.pop("age")                           # prints {'id': 112, 'city': 'sydney'} -  removes the key and return its value, or return your default if the key is missing
# or
# # # return error if not a key so use :-
age = user.pop("age", "not found")
print(user)  
print("removed item:", age)                             

# popitem - returns and delete the most recent key value pair from the dict
user.popitem()
print(user)        # {'id': 112, 'age': 33}

########## creation #########

# fromkeys() - bui;d a new dict where all keys get the same default value
user = {'id' : None, 'age' : None, 'city' : None}

user = dict.fromkeys(["id", "name", "age", "city"], None)
print(user)


####### use case ######
# 1. database or api records- returns records are stored as dict where column names are keys and row value are dict value.
# 2. mapping to friendly value - great for converting technical code into friendly labels.
# 3. mapping abbreviations - turning short abbreviations into full readable names.
# 4. config and environment - store system setting like host ports and username in one clean place.
#5. etl and pipeline setting 


###### challenge #####
user = {"id" : 1, "name" : "mike", "age" : 30, "city" : "goa"}
# # 1. create a new dict
# # 2. keep only pairs with string Value
# # 3. convert value to upper case
# # 4. elegent value and short solution

user1 = {
    key: value.upper()
    for key , value in user.items()
    if isinstance(value , str)
    }
print(user1)