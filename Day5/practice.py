# # Validate : user name
# # Must not be empty
# # Must be between 3 and 15 characters
# # Must not contain spaces
# # Must start with a letter
# # Must not be same as password
# # Must be all lowercase

username = "ayushigupta"
password = "ayugupta"
if username == "":
    print("Username required")
elif len(username) > 15 or len(username) < 3:
    print("Username must be 3 to 5 characters")
elif ' ' in username: 
    print(" No spaces please")
elif not username[0].isalpha():
    print("should start with letter")
elif username == password:
    print("username and password should not be same")
elif username != username.lower():
    print("username should be lower case")
else:
    print("Valid username")



# #Question 2: Validate a Phone Number
# Must not be empty
# Must be exactly 10 digits
# Must contain digits only (no letters or symbols)
# Must not start with 0
# Must not contain spaces

phonenumber = "5730270953"
if phonenumber == "":
    print("phone number empty")
elif len(phonenumber) != 10  :
    print("phone no must be 10 digits")
elif not phonenumber.isdigit():  # You don't compare phonenumber to .isdigit() — only it returns True/False 
    print("must contains digit only") 
elif phonenumber[0] == "0":
    print("Must not start with 0")
elif ' ' in phonenumber:  #This will never trigger because .isdigit() already catches spaces (spaces aren't digits). Move it before the .isdigit() check — or just remove it since isdigit handles it.
    print("must no contain spaces")
else :
    print("valid phone number")


# Question 3: Validate an Age
# Must not be empty
# Must be a number
# Must be between 18 and 100
# Must not be negative
# Must not be a decimal (must be whole number)

age = "23"
if age == "":
    print ("age must not be empty")
elif age.startswith("-"):
    print("must not be negative")
elif '.' in age:
    print("must not be a decimal")
elif not age.isdigit():
    print("contain numbers only")
elif not 18 <= int (age) <= 100  :
    print ("age must be betweeen 18 to 100")
else:
    print ("valid age")

# # order of checks is wrong
# #Check decimal and negative before .isdigit()
# #Convert to int() only after confirming it's a digit



# Question 4: Validate a PIN
# Must not be empty
# Must be exactly 4 characters
# Must contain digits only
# Must not be all same digits (like 1111, 0000)
# Must not be same as age

pin = "2345"
age = "2347"
if pin == "":
    print ("pin must not be empty")
elif len(pin) != 4:
    print ("pin must be exactly 4 char")
elif not pin.isdigit():
    print("contain digit only")
elif pin == age :
    print ("pin and age not be same ")
elif pin[0] == pin[1] == pin[2] == pin[3]:
    print("must not be all same digits")
else:
    print ("valid pin")


# Question 5: Validate a Full Name
# Must not be empty
# Must be at least 3 characters
# Must contain at least one space (first and last name)
# Must not contain digits
# Must not contain special characters like @, #, !
# Must start and end with a letter

Valid_full_name = "Ayushi gupta"
if Valid_full_name == "":
    print("Full name must not be empty")

elif len(Valid_full_name) < 3:
    print("Must be at least 3 characters")

elif not " " in Valid_full_name:
    print("Must contain at least one space (first and last name)")

elif not Valid_full_name[0].isalpha() or not Valid_full_name[-1].isalpha():
    print("Must start and end with a letter")

elif any(c.isdigit() for c in Valid_full_name):
    print("Must not contain digits")

elif not all(c.isalpha() or c == " " for c in Valid_full_name):
    print("Must not contain special characters")

else:
    print("Full name valid")


# # Question 6: Validate an Email
# Must not be empty
# Must contain exactly one @
# Must contain a . after the @
# Must not contain spaces
# Must not start with @
# python email = "ayushi@gmail.com"
# Expected output: Valid email

mail = "ayushi@gmail.com"
if mail == "" :
    print("must not be empty")
elif mail.count('@') != 1:
    print("must contain exactly 1")
elif mail.index('@') > mail.index('.'):
    print("Must contain a . after the @")
elif ' ' in mail:
    print("Must not contain spaces")
elif mail[0] == '@':
    print("Must not start with @")
else :
    print("valid mail")

# -for this specific email there is no problem! other wise order issue
# The logic is correct but order is the issue!


# Question 7: Validate a Username
# Must not be empty
# Must be between 5 and 15 characters
# Must not contain spaces
# Must start with a letter
# Must contain letters and numbers only (no special characters)
# python username = "ayushi123"
# Expected output: Valid username



# Question 8: Validate a Password
# Must not be empty
# Must be at least 8 characters
# Must not contain spaces
# Must contain at least one digit
# Must not be same as username
# python password = "ayushi123"
# username = "ayushi"
# Expected output: Valid password

# Tips before you start:
# TaskMethod to use
# check lengthlen()
# check digits only.isdigit()
# check letters only.isalpha()
# check space' ' in x
# check start/end x[0] and x[-1]
# check all lowercase x == x.lower()
# check whole numberisinstance(x, int)


