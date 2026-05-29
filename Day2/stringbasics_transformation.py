# # two build in function to handle the string data type 
# # type() and str()

# name = "dharmesh"
# print(type("name"))
# # or 
# print(type(name))
# #both works

# age = 24 
# print(type(age))
# print("your age:", age)

# print("your age is:" + age) # trying to add string and int, an only concatenate str (not "int") to str

# # str()
# age = 24 
# print(type(age))
# print("your age:", age)
# print("your age is:" + str(age)) # we just changes the data type just to print; orignally it is a integer as declared above; it doesnt change the data type of variable.
# print(type(age))

# age = 24
# age = age + 6
# print(age)
# # if we convert the variable to data type str()
# age = str(age) 
# print(type(age)) # type() becomes str 
# age = age + 5 #can only concatenate str (not "int") to str; as we have changed the data type in line 27

# #maths- len() and count()
# #len
# password = "asdfg1"
# print(len(password))
# len count everthing even space 
# if len(password) < 8:
#     print("password to short")

# #count - count the frequency of string 
# #usecase - detect the unwanted character in my data

# text = """i got to Gym
# everyone should go to gym atleast 4 days a week
# there are 10 machine in gym
# everyone should go to gym in a evening time"""
# print(text.count("gym")) # it is case sensative.

# text = """i got to Gym$ls
# everyone should go to gym atleast 4 days a week$
# there are 10 machine in gym
# everyone should go to gym in a evening time"""
# print(text.count("$")) # it is case sensative.


# # Transformation - replace(), split(), concatenation "{h} + {i}"", f-string, repetation {h} * 2 :

# price = "1232.32112"
# print(price.replace("." , "$"))

# date = "20/10/1990"
# print(date.replace("/" , "-"))

# phone = "910-4902-231"
# print(phone.replace("-" , ""))      # replace by empty/no space and "-"

# price = "$1,212.99"
# print(price.replace("$" , "").replace("," , ""))



########################################### challenge exercise ##################################################

# phone = "+49 (176) 123-4567"
# print(phone.replace("+" , "00").replace(" (" , "").replace(") " , "").replace("-" , ""))

#################################################################################################################

# #concatenation 
# #just adds two string directly 

# first_name = "ayushi"
# last_name = "gupta"
# full_name = first_name + last_name
# print(full_name)
# full_name = first_name + " " + last_name
# print(full_name) 

# #usecase 
# folder = "c: Users/dharmeshchaudhary/Material/Python/Day2/"
# file = "stringbasics_transformation.py"
# full_file_path = folder + file
# print(full_file_path)

##### f-string 

# name = "ayushi"
# age = 22
# is_student = False
# #print("My name is " + name + "I am " + age + "years old, and student status is" + is_student + ".") # doesnt work as diff data types
# #print("My name is " + name + " I am " + str(age) + " years old, and student status is " + str(is_student) + ".") #can only concatenate str (not "bool") to str
# #to lengthy and hard to read, worry about space

# print(f"My name is {name}. i am {age} year old, and student status is {is_student}.")

# # #{} aere used for expression 
# print(f"2 + 3 = {2 + 3}")

# print(f"{{this is me}}")

# split()
# stamp = "2020-09-16 14:30"
# print(stamp.split(" "))
# stamp = "2022 02-10 16:23"
# print(stamp.split(" "))
# stamp = "2020-02-29"
# print(stamp.split("-"))

# csv_file = "1234,max,aus,1988-19-20,M"
# print(csv_file.split(","))

# #Transformation string repetition
# #repeting the string value with numbers --> just repeat
# print("ha" * 8)
# print("###" * 20)

############
word = "It got dark as the sun set"
new = word.split(" ")
print(new)
