
#################################### Nested and Advance conditions ####################################

# #nested if
# #if, if statement is true then check the second if 
# # each if statement has its own else statement 

# score = 90
# project = False
# if score >= 90: 
#     if project:  # python evaluates boolean condition directly avoid explicit comaparison == True or ==false.
#         print("+A") 
#     else:
#         print("A")
# else:
#     print(False)        

# #conditions in same if statement 
# #connecting two condition in the same if statement, using logical operator. 
# # and & or operator: and return true only when both the conditon are true.

# score = 90
# project = True
# if score >= 90 and project: 
#      print("+A")
# else:
#     print("A")     

# score = 80
# project = False
# if score >= 90 and project: 
#      print("+A")
# elif score >= 90:
#      print("A") 
# elif score >= 80 and project:
#      print("+B")
# else:
#      print("B")

# score = 49
# project  = False  
# if score >=50 and project:
#     print("outstaning")
# elif score >= 50 and not project:
#     print("Good")
# elif score < 50 and project:
#     print("pass")
# else:
#     print("fail")        

# #independent if 
# #each if is checked separately: all condition are tested - even if one is already true.
# they dont have dependency on each other.

score = 49
project = False
if score >= 50:
    print("High score")
else:
    print("Low score")

if project:
    print("Project submitted")
else: 
    print("Project not submitted")

