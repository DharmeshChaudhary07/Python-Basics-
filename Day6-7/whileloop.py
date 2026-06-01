
################################################# While loop #################################################\

# # while loop- repeat the block of code over and over until condition is true
 
# i = 1.  # initialization
# while i < 5: #condition
#     print(i) 
#     i += 1  #update

# # task write a program that keeps asking do you agree? until the user types yes
# answer = ""
# while answer != "yes":
#     answer = input("do you agree?:")
# print("thank you")

# while True:
#     answer = input("do you agree?:")
#     if answer == "yes":
#         break
# print("thankyou")


# # Limit user to 3 attempts only

# attemps = 0
# while attemps < 3:
#     answer = input("do you agree?:")
#     if answer == "yes":
#         break
#     attemps = attemps + 1
# print("thankyou")

# # If the user types yes before 3 attempt print Glad we are on same page!

# attemps = 0
# while attemps < 3:
#     answer = input("Do you agree :")
#     if answer == "yes":
#         print("We are on the same page")
#         break
#     attemps += 1
# print("thankyou")

# # other wise print "3 strikes, you are out!"

attemps = 0
while attemps < 3:
    answer = input("Do you agree :")
    if answer == "yes":
        print("We are on the same page")
        break
    attemps += 1
else:
    print("3 strikes, you are out!")
    

