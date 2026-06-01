
####################################### Loops ########################################
# # loops control the flow of code - repeat a block of code over and over until condition is met.

# # For loop
# # go through the group of item one by one to do something for each item
# # for i in (1,2,3):
# #    print("i")

# for i in (1,2,3):
#    print("i")

# print("round : 1")
# print("round : 1")
# print("round : 1")
# print("round : 1")
# print("round : 1")

# # #or

# print("round : 1")
# print("round : 2")
# print("round : 3")
# print("round : 4")
# print("round : 5")

# #or instead 

# for i in (1,2,3,4,5):
#    print(f"round {i}") #f-string (formatted string literal) — a Python feature that lets you embed expressions directly inside a string using {}.

# items = (1,2,3,4,5) 
# for item in items:
#    print(f"round {item}") # use the same words variable --> singular, sequence --> plural

# # Sequences you can loop :
# # file, tuple, list, string, dict, range etc.
# # any object in python which is iterable can be used in sequence.
# # for loop--> we have to always specify the sequence (a group of item that has start and end).

# #tuple
# items = (1,2,3,4,5) 
# for item in items:
#    print(f"round {item}")

# # #list
# items = [1,2,3,4,5] 
# for item in items:
#    print(f"round {item}")

# #string
# items = "python"
# for item in items:
#    print(f"round {item}")

# #range
# for item in range(8):
#    print(f"round {item}") # #it starts with 0, so will not include 8 (till 7 only)

# # we can specify the start point in the range --> it will start where you specify but it will not include stop
# for item in range(16,20):
#    print(f"round {item}")

# #we can also add steps
# for item in range(0,20,2):
#    print(f"round {item}") # even numbers

# for item in range(1,20,2):
#    print(f"round {item}") # odd numbers

# # use case 

# scores = [30 ,10 ,90, 70, 50]
# total = 0
# for score in scores:
#     #total = total + scores # use the loops not the sequence (total = total + scores)
#     total = total + score
#     print("Total score:", total)
# print("Final total" , total)

# #cleaning data
# files = ['ReporT.csv  ', '  DaTa.CSV', 'final.TXT']
# for file in files:
#     file = file.strip().lower().replace('.txt', '.csv')
#     print("New file" , file)

# print 7 table (eg. 7 * 1 = 7)
tables = 7
for table in range(1, 11):
    total = table * tables # — no need for extra variables when you can just compute directly inside the f-string. 
    print(f"7 * {table} = {total}")

# # #more simple way

# for table in range(1, 11):
#     print(f"7 * {table} = {7 * table}")

# #print a left aligned pyramid of star with 6 rows using loops

# for i in range(1,7):
#     print(i * "*")

# for i in range(1,7):
#     print(" " * ( 6 - i) + i * "*")
    