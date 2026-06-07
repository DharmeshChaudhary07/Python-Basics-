
# ######################################################### Parameters, Arguments and Return ##########################################################

# ######################################################################################################################################################

# # functions can be of diff type -> no input or output, only input, input and output, mutliple input and output.

# # Parameter: 
# # data which goes in as input is called parameter and data which comes out it called return.
# # Parameters: Name used in function defination that describes what data the function expects. acts like a placeholder.

# # syntax:
# def multiply(x):   # x is a parameter 
#     print(x * 2)
# multiply(3)        # 3 is a argument

# def clean_text():                # basic
#     name = "  MariA  "
#     print(name.strip().lower())
# clean_text()
# #
# def clean_text(name):            # using parameter and arguments
#     print(name.strip().lower())
# clean_text("  MariA ")
# clean_text(" bObindEr ")


# # Function parmeter-> Scope -> 1. parameter 2. local variable 3. global variable. 
# #                  -> Default parameter

# f = 2                          # f = global variable
# def multipy(x):                # x = parameter 
#     y = f * x                  # y = local variable
#     print(y)
# multipy(3)                     # 3 = argument

# # after code is executed --- local variable and parameter is destroyed. (argument is just a value, not a variable that lives inside a function).

# case_rule = "lower"
# def clean_text(name):            
#     cleaned = name.strip()
#     if case_rule == "lower":
#         cleaned = cleaned.lower()
#     print("cleaned:", cleaned)
# clean_text("  MariA ")
# clean_text(" bObindEr ")


# # A default parameter is a parameter that has a pre-set value — if no argument is passed, it uses the default value.
# def make_coffee(cup_size, sugar=2):  # sugar has default value 2
#     print(f"{cup_size} coffee with {sugar} sugar")
# make_coffee("large")        # no sugar argument → uses default 2
# make_coffee("medium", 4)


# #####################################################################################################################################################

# # Arguments:
# # Arguments: actual values passed in the function call that are assigned to parameters


# def clean_text(name, lastname, country):           
#     first = name.strip().lower()
#     last = lastname.strip().lower()
#     place = country.strip().lower()
#     fullname = first + " " + last
#     print(fullname , "from" , place)
# clean_text("  MariA ", " singH ", "Canada")


# # types of Argument: 
# # 1. Positional argument
# # 2. Keyword argument
# # 3. Mixed → combination of above
# # 4. flexiblity -> 1. *args  → variable length argument
# #               -> 2. kwargs → keyword variable length argument

# def clean_text(name, lastname, country = "na"):           
#     first = name.strip().lower()
#     last = lastname.strip().lower()
#     place = country.strip().lower()
#     fullname = first + " " + last
#     print(fullname , "from" , place)

# # postional argument ( the order of argument must match the order of parameter)
# clean_text("  MariA ", " singH ", "Canada")

# # keyword argument (No need of order, it knows value is for which parameter)
# clean_text(lastname = " singH ", country = "Canada", name = "  MariA ")
  
# # mixed argument (postional argument must be before keyword arguments)
# clean_text("  MariA ", lastname = " singH ", country = "Canada")
 
# # default parameter (default parameter should be last in the function defination after all the parameter which has no default value)
# clean_text("  MariA ", " singH ",)



# # # flexiblity arguments 
# # # Allow function to accept a unknown number of arguments.
# # # *args for positonal arguments
# # # **kwargs for keyword argument

# def total(a , b, c, d):
#     print(a+b+c+d)
# # total(1,2)
# # total(1,2,3)
# total(1,2,3,5)    # every time we need to change code inside the function.


# def number(*args):
#     print(type(args))    #tuple
#     print(sum(args))
# number(1,2,3)

# def name(**kwargs):
#     print(type(kwargs))     #dict
#     print(kwargs)
# name(name = "ellie balish", country = "uganda", age = 92)
# name(name= "Mo", age = 56)

# ###################################################################################################################################################

# # 
# # Return
# # return is a keyword or a statement its not a function.
# # used to exit the function and send back to the caller.
# # store the value returned by "return" .  # # assign a call function to a variale to store the returned. 

# def greet(name):
#     print("Hello", name)   # just prints, no return
# result = greet("jayabachan")    # Hello Alice
# print(result)         # prints none

# def greet(name):
#     print("Hello", name)   # just prints, no return
#     return name
# result = greet("jayabachan")    # Hello Alice
# print(result)    # prints alice

# # function can have multiple return statement
# def greet(name):
#     if not name:
#         return None
#     cleanedlower = name.strip().lower()
#     cleanedUpper = name.strip().upper()
#     return cleanedlower, cleanedUpper
# result = greet("jayaA")  # prints none as string is empty
# print(result)   

# ###################################################################################################################################################
