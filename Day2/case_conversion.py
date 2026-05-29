##### case conversion : upper() and lower()

# text = "python PETER OF KENSINGTON"
# print(text.upper())
# print(text.lower())

#### use case
# # example 1
# search = "email"
# data = "Email"
# print(search == data)
# print(search == data.lower())

# # example 2
# search = "      email"
# data = "Email    "
# print(search == data)
# print(search.strip() == data.lower().strip())

################################### challenge exercise ####################################

# we have a messy string "968-Maria, ( D@t@ Engineer ) ;; 27y  " --->>> name: maria | role: data engineering | age: 27

# text = "968-Maria, ( D@t@ Engineer  ) ;; 27y  "
# #### thew worst way i could do this 
# print("name: ", text.lstrip("968-").rstrip(", ( D@t@ Engineer  ) ;; 27y)") , "|" , "role: " ,text.replace('@','a').lstrip("968-Maria, ( ").rstrip(" ) ;; 27y  ") , "|" , "age: " , text.lstrip("968-Maria, ( D@t@ Engineer  ) ;;").rstrip("y  "))
# ####

text = "968-Maria, ( D@t@ Engineer  ) ;; 27y  "
name = text[text.index('-')+1 : text.index(',')]
print(name)
role = text[text.index('(') + 2 : text.index('  ')].replace('@','a')
print(role)
age = text[text.index(';')+3 : text.index('y')]
print(age)
print("name:" , name , "|" , "role:" , role , "|" , "age:" , age)

############################################################################################


