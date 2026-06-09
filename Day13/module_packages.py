
# ####################################################################### Modules ##################################################################################

# # module 
# # Consider a module to be the same as a code library.
# # A file containing a set of functions you want to include in your application.

# # Now we can use the module we just created, by using the import statement:

# import mymodule  # Import the module named mymodule, and call the greeting function:
# mymodule.greeting("Jonathan")

# # Note: When using a function from a module, use the syntax: module_name.function_name.

# ###################################################################################################################################################################

# # import variable in modules

# # The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

# import mymodule          # Use import module when you're using multiple things from it, or when the source of the name should stay visible in the code
# a = mymodule.person1["age"]
# print(a)
# # or
# from mymodule import person1    # Use from module import something when you need one or two specific things and the name makes it obvious where it came from (e.g. from math import sqrt)
# a = person1["age"]
# print(a)

# # we can import multiple variable from module at once.
# from mymodule import person2, person3
# a = person2["name"]
# print(a)
# b = person3["country"]
# print(b)

# ###################################################################################################################################################################

# # Naming a module 
# # You can name the module file whatever you like, but it must have the file extension .py
# # renaming a module 
# # we can create an alias when you import a module, by using the as keyword:

# import mymodule as mm
# a = mm.person2["name"]
# # a = mm.person2["name"] mm.person3["country"]
# print(a)

# ###################################################################################################################################################################

# # There are several built-in modules in Python, which you can import whenever you like.
# # like system, math, os , random, datetime, time (more than 200 built in module in python which can be imported)

# import platform
# x = platform.system()
# print(x)

# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
# import mymodule
# x = dir(mymodule)
# print(x)    # prints ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'greeting', 'person1', 'person2', 'person3'] 
# # prints variable names which we defined and dunder attributes
# print(mymodule.__file__)    # Those are called dunder attributes (double underscore = "dunder") — Python automatically adds them to every module. They contain metadata about the module itself.

# import platform
# x = dir(platform)
# print(x)

# ###################################################################################################################################################################

# # using from
# # You can choose to import only parts from a module, by using the from keyword.
# # Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]

# from mymodule import person1
# print(person1["age"])     # prints 36
# print(person1)    # prints {'name': 'John', 'age': 36, 'country': 'Norway'}

# ###################################################################################################################################################################

# # We use if name == "main": to test our module's code without affecting other files.We use if __name__ == "__main__": to test our module's code without affecting other files.
# # That's it.
# # When you're building mymodule.py you want to quickly check — "is my function working? is my variable correct?" — so you test it right there at the bottom.
# # But when main.py imports mymodule, that test code stays silent and doesn't interfere.

############# this should be in mymodule.py #############
## mymodule.py

# def greeting(name):
#     print("Hello, " + name)
# if __name__ == "__main__":
#     greeting("Jonathan")  # ← just checking it works 

############# should be here only #############
import mymodule
mymodule.greeting("Alice")  # ← now using it for real