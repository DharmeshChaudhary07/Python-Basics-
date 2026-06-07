
############################################################### Type of function (baed on purpose or usecase) ##############################################################
 
# # Type of function ( Based on purpose or usecase)
# # 1. Action
# # 2. Transformation
# # 3. Validation
# # 4. Orchestrator



# # Action function
# # Designed to perform operation in the system instead of returing value 
# # like print output, save data to database, send email if something goes wrong, calling a api
# # Also called as command function, handler function, service function, side effect function.

# # Task: store application log message in file whenever an event occurs
# def write_log(message):
#     with open("/Users/dharmeshchaudhary/Material/Python/Day8/app.log", "a") as file:
#         file.write(message)
# write_log("hello, rakhi sawant" + "\n")
# write_log("Welcome rakhi"  "\n")
# write_log("Wanna meet deepak kalal?"  "\n")



# # Transformation 
# # raw data as input, gets transformed, and returns processed data
# # like data manipulation, bussiness logics
# # Also called data function, mapper function, utlity function

# # Task: Cleaned email address and return username and domain name
# def clean_and_split_email(email):
#     clean_email = email.strip().lower()
#     username, domain = clean_email.split("@")
#     return {"username" : username, "domain" : domain}
# print(clean_and_split_email("rakhi.deepak@gmail.com"))



# # Validation
# # Validate a conditon and returns the boolean. (doesnot change data/it doesnot have action).
# # like check user input, check business rule, user permission.
# # also called checker function.

# # Task1: Check the if a password meets the minimum length of 8.
# def is_valid(password):
#     return len(password) >=8
# print(is_valid("12345678"))

# # Task2: check if email is valid
# def is_valid_email(email):
#     return "@" in email and "." in email 
# print(is_valid_email("rakhi.deepak@gmail.com"))
# print(is_valid_email("rakhi.deepakgmail.com"))



# # Orchestrator  
# # Controls program flow by calling other function in the correct order.
# # Also called controller function, spipeline function, workflow function

# # Task: 1.    Receive an email from the user
# #       2.    Validate the email
# #       3.    If it is invalid, Log an error in a file.
# #       4.    If it is valid, Clean and structure the email.
# #       5.    Log each step of the program.
  
def write_log(message):
    with open("/Users/dharmeshchaudhary/Material/Python/Day8/app.log", "a") as file:
        file.write(message + "\n")

def is_valid_email(email):
    return "@" in email and "." in email 

def clean_and_split_email(email):
    clean_email = email.strip().lower()
    username, domain = clean_email.split("@")
    return {"username" : username, "domain" : domain}

# orchstrator function
def process_user_email(email):
    write_log("app started")
    # # 2.    Validate the email
    # #  is_valid_email(email) # useless, If you are not storing or using the result of a function call immediately — it is always useless and can be removed.
    # 3.    If it is invalid, Log an error in a file.
    if not is_valid_email(email):
        write_log(f"Invalid email: {email}")
    # 4.    If it is valid, Clean and structure the email.
    else:
        clean_email = clean_and_split_email(email)
        # 5.    Log each step of the program.
        write_log(f"Processed email: {clean_email}")
    write_log("app stopped")

# 1.    Receive an email from the user 
email = input("Write your email address: ")
process_user_email(email)
 