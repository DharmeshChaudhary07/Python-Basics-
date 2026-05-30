
################################### Membership operator #######################################

# # not not in

# print("q" in "ayushi")
# print("q" not in "ayushi")

####### Uses case #######
# # validate that the domain is not on the banned list

# domain = "gmail.com"
# banned_domain = ["outlook.com" , "insta.com", "meta.com"]
# print(domain in banned_domain)
# print(domain not in banned_domain)


################################### Idendity operator ##########################################

# # is, is not 
# # checks if two variable refers to the same object in the memory
# # just compare the objectid not the value of the variable

# domain = ["outlook.com" , "insta.com", "meta.com"]
# banned_domain = ["outlook.com" , "insta.com", "meta.com"]
# print(domain == banned_domain)
# print(domain is banned_domain) # as it is stored at differnt object in the memory.

# a = 5
# b = 5
# print(a == b)
# print(a is b) # as it is a very simple value, it will store value at same objectid in the memory

# a = ["5", "7" ,"10"]
# b = a
# print(a == b)
# print(a is b) # assigns one variable to the same object that another variable is referring to

####### practice exercise #######
# #validate the email address it must be filled in and not not empty

# email = ""
# print(email != "")

# mail = "b@gmail.com"
# print(mail != "")

# mail = None
# print(mail != "") # return true but should be false 
# print(email != None and email != "")
# print(email is None and email != "")


################################## challenge exercise ##########################################

            ######################################################################
# check if a user name is not empty and age is greater than equal to 18
# check if the password is atleast 8 characters long and does not contain space 
# check if a user email is not empty contains @ and ends with .com
# check if a username is a string, is not None, and is longer than 5 character
# check if the user is either an admin or a moderator and either they are not banned or they have verified their email
            ######################################################################

# username = ["bob", "tom", "sam"]
# age = 19
# print(username != "" and age >= 18)  
# # print(bool(username) and age >= 18) # username is a list, not a single username string. bool(["bob", "tom", "sam"]) is True simply because the list is non-empty — it has nothing to do with whether a username is valid.
# #print( username != 0 and age >= 18) # compares list to a number # not correct pythonically

# password = "dharmesh"
# print(len(password) >= 8 and ' ' not in password)

# email = "data@abc.com"
# print(email != [] and '@' in email and email.endswith(".com"))

# username = "bobender"
# print(isinstance(username, str) and username is not None and len(username) > 5)

# username = "admin"
# isbanned = True
# isverified = False
# print((username in ["admin", "moderator"]) and (not isbanned or isverified)) #print(username in ["admin" or "moderator"]) only check the admin 

#################
# #"admin" in ["admin", "moderator"]
# #asking → "is the string admin sitting inside this list?"  → Yes 
# #username = "admin"        # string 
# #["admin", "moderator"]    # list 
# #username doesn't need to be a list — in just checks "does this item exist inside this list?"

# #PriorityOperatorHigher (binds first)in, not in, ==, != and Lower for or, and also and has high priority than or 

##################