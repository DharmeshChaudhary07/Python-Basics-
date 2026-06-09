
############################################################## Exception Handling #############################################################################

# Errors and exceptions are both issues in a program, but they differ in severity and handling.
# Error: Issues in the program logic such as SyntaxError, etc. It occurs at compile time.
# Exception: Problems that occur at runtime and can be managed using exception handling (e.g., invalid input, missing files).


# exception handling : When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

#############################################################################################################################################################

# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.


table = input("enter the number: ")
print("multipication of table")
try:
    for i in range(1,11):
        print(f" {int(table)} * {i} = {int(table) * i}")

# except Exception as e:   # invalid literal for int() with base 10: 'daini'
#     print(e)

except:
    print("error occured need a int as input")



try:
    l = [1,3,4,6,7]
    i = int(input("Enter a number:"))
    print(l[i])
except: 
    print("some error occured") 
else : 
    print("all good man")               # works only when there is no error from try: and except:



try:
    l = [1,3,4,6,7]
    i = int(input("Enter a number:"))
    print(l[i])
except: 
    print("some error occured")       

finally: 
    print("i am always exceuted")

# print("i am always exceuted")             # but i can write this too , this also exceute every time?
#                                           # no we cannot : doenot work in function 
# Situation                finally runs?
# No error                 ✅ Yes               
# Error occurs             ✅ Yes
# return in try            ✅ Yes
# return in except         ✅ Yes
# Outside function print   ❌ Not guaranteed                                        

#############################################################################################################################################################

# Catching Specific Exceptions

try:
    l = [1,2,3]
    i = int(input("index:"))
    print(l[i])
except ValueError:
    print("value error")
except IndexError:          # 3 -> prints index error 
    print("index error")
except ZeroDivisionError:
    print("division error")


# Common exceptions to know:
# Exception                                      When?

# ValueError                                wrong value type 
# TypeError                                 wrong data type
# IndexError                            list index out of range
# KeyError                                dict key not found
# ZeroDivisionError                         divide by zero
# FileNotFoundError                         file not found

# from Claude :

# try:
#     l = [1, 2, 3, 4, 5]
    
#     i = int(input("Enter index: "))  # ValueError
    
#     result = l[i] / 0               # ZeroDivisionError / IndexError
    
#     d = {"name": "raj"}
#     print(d["age"])                  # KeyError

# except ValueError:
#     print("Enter a valid number!")

# except IndexError:
#     print("Index out of range!")

# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# except KeyError:
#     print("Key not found in dictionary!")

# except TypeError:
#     print("Wrong data type used!")

# except FileNotFoundError:
#     print("File not found!")

# except Exception as e:
#     print("Unknown error:", e)       # catches anything else

# else:
#     print("No error occured!")

# finally:
#     print("Always runs!")

#############################################################################################################################################################

# raise : The raise keyword is used to raise an exception
# we can define what kind of error to raise, and the text to print to the user.
# we can use any of the exception from class exception or user can define in class to custom exception.

# raise 

age = int(input("Emter your age must be greater than 18 and less than 25: "))

if not (age > 18 and age < 25):
    raise ValueError("must be greater than 18 and less than 25")



# # Custom error example
class AgeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    age = int(input("Enter age: "))
    if age < 0:
        raise AgeError("Age cannot be negative!")
    print("Age:", age)

except AgeError as e:
    print(e)

#############################################################################################################################################################