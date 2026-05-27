input("enter you name:") # just stores, does not display 

name = input("enter you name:")
print(name)    # displays

name = input("Enter you name:")
print("My name is" , name)

name = input("Enter you name:")
country = "australia"
print(name , " comes from" , country)      



# # Hardcoded value 
# variable which are defiend in the code 

name = input("enter your name:")
country = "India"
print(name ," comes from ", country)

# # Dynamic value 
# value depend on the user input 

x = "A"
print(x)
y = input("Enter the value: ")
print (y)


# # Data type

a = 10      #interger
b = 3.14  #float
c = "hello"  #string
d = 'hello' #string
e = "1234"  #still a string
f = True  #bool
g = False  #bool
h = None #empty and no data type declared yet 
i = ""  # blank string without character inside its not same as none 
j = " " # white space " " is string value woth 1 or more spaces not same as none

# why do we need data type-
print(2+3)  #integer function
print("2" + "3") # string function

# using function and method together
Text = "hibaby"
Number = 142
print(Text)
print(Number)

print(type(Text))
print(type(Number))

print(len(Text))
print(len(Number))     ###### len doesnot work with integer

################################## Methods ##################################

Text = "hibaby"
Number = 123
Text.upper()
print(Text.upper()) # Number.upper()-----> doesnt work with int 
print(Number.bit_length()) # print(Text.bit_length()) doesnt work with strings

############################################################ challenge exercise #################################################################


your_age = 26
your_height = 5.7
your_name = "Dharmesh"
ru_student = True
no_value = None

print(your_age)
print(your_height)
print(your_name)
print(ru_student)
print(no_value)

print(type(your_age))
print(type(your_height))
print(type(your_name))
print(type(ru_student))
print(type(no_value))

#print(len(your_age))
#print(len(your_height))
print(len(your_name))
#print(len(ru_student))
#print(len(no_value))

####################################################################################################
# input function always return string 

age = input("Your age:")
height = input("Your height:")
name = input("Your name:")
student = input(" Are you student:")

print(" Variable:", age)
print(" Data type:", type(age)) # returns string, but we have a age as integer: doesnt work
print(" Data type:", type(int(age))) # to print a int in a input function
print(" Length:", len(age))

print(" Variable:", height)
print(" Data type:", type(height)) #doesnt work as- input function doesnt return float
print(" Data type:", type(float(height))) 
print(" Length:", len(height))

print(" Variable:", name)
print(" Data type:", type(name)) 
print(" Data type:", type(float(name)))
print(" Length:", len(name))

# for bool - input function doesnt take user input it has to be defined in the code
print(" Variable:", student)
print(" Data type:", type(student)) #doesn't work as- inputfunction doesnt return float
print(" Length:", len(student))

# input function does not work with a no value/ none - should be defined in the code

################################################################################################