
######################################## Inline if and Match case ###################################

# #inline if (ternary)
# # instead of writing multiple line: we can use inline if
# # Syntax: do A if conditon1 else do B.  #quick and short #output of inline if will be stored in a variable. 
# # cannot skip else here "must": include both if and else.
# # if we have multiple condition we cannot use elif. # #only use when logic is very simple

# score = 79
# "outsanding" if score >= 80 else "pass" # no action as it stored in a variable
# # # or
# print("outsanding" if score >= 80 else "pass")
# # # or
# grade = "outsanding" if score >= 80 else "pass"
# print(grade)

# score = 79
# grade = "A" if score >=90 else "B" if score >= 80 else "pass"
# print(grade)

# # Match case
# # can be used only for matching values: 
# # evaluates a exact value againts multiple value - Runs the code of the first match
# # syntax:- 
# # value = ""
# # match value:
# #         case "":
# #.            print("")
# #.        case _: 
# #             print("non match")

# # works only for python version 3.10+
# country = "ind"
# match country:
#     case "USA":
#         print("US")
#     case "india":
#         print("IN")
#     case "germany":
#         print("GER")
#     case _:
#         print("No country match")

# # easy to read and write 
# # instead of using. multiple condition in code: 
# # can be used only for matching values

# country = "Ind"
# match country:
#     case "USA":
#         print("US")
#     case "india" | "Ind":
#         print("IN")
#     case "germany":
#         print("GER")
#     case _:
#         print("No country match")

########################################## Challenge exerice ##########################################
# #1. validate the quality and correctness of email values
# #- must not be empty
# #- must contain '.' and '@'
# #- must contain exaclty one '@' symbol
# #- must end with '.com', 'org' or '.net'
# #- must no be longer that 254 charcters
# #- must start and end with a letter or digit

# email = " bobinder@gmail.com"
# email = email.strip()
# if email == "":
#     print("email is empty")
# elif not('.' in email and '@' in email):
#     print("must contain . and @")
# elif email.count('@') != 1:
#     print("must contain exactly one @")
# elif not (email.endswith(".com") or email.endswith(".org") or email.endswith(".net")):
#     print("must end with .com, .org or .net")
# elif len(email) > 254:
#     print("must not be longer than 254 characters")
# elif not email[0].isalnum() or not email[-1].isalnum():
#     print("must start and end with letter or digit")
# else:
#     print("email is valid ")

# #2. validate the quality od correctness of passwards
# # must not be empty
# # must be atleast 8 characters
# # must include atleast one upper case
# # must include atleast one lower case
# # must not be same as email
# # must not contain any spaces
# # must start and end with numbers or letter 

# password = "Cdharmesh"
# email = "Cdharmesh@gmail.com"

# if password == "":
#     print("password is empty")
# elif len(password) < 8:
#     print("must be at least 8 characters")
# elif password == password.lower():
#     print("must include at least 1 uppercase")
# elif password == password.upper():
#     print("must include at least 1 lowercase")
# elif password == email:
#     print("password must not be same as email")
# elif ' ' in password:
#     print("password must not contain spaces")
# elif not password[0].isalnum() or not password[-1].isalnum():
#     print("must start and end with a letter or digit")
# else:
#     print("valid password ")
########################################################################################################

# independent if

email = " @bobinder@gmail.com"
email = email.strip()
valid = True
if email == "":
    print("email is empty")
    valid = False
if not('.' in email and '@' in email):
    print("must contain . and @")
    valid = False
if email.count('@') != 1:
    print("must contain exactly one @")
    valid = False
if not (email.endswith(".com") or email.endswith(".org") or email.endswith(".net")):
    print("must end with .com, .org or .net")
    valid = False
if len(email) > 254:
    print("must not be longer than 254 characters")
    valid = False
if not email[0].isalnum() or not email[-1].isalnum():
    print("must start and end with letter or digit")
    valid = False
if valid:
    print("email is valid")

