
######################################## Conditional Statement ###################################

# #if statement
# #define the condition first, then if true do this -otherwise (false) then do nothing.
# #standalone 
# #always comes first 

# score = 100
# if score >= 90:
#     print("A") 

# #space before print is called indentation 
# #indentation : adding space at the beginning of a line to show that the line belongs to a code block
# #spaces are part of the syntax (nesting of a code)


# #else statement
# #if the if condition in True/false then do this: runs one path only
# #not standalone 
# #always comes after if statement
# #doesnt accept condition 

# score = 80
# if score >= 90:
#     print("B")
# else :
#     print("False")


# #elif statement
# #only runs lif follow up condition false
# #comes after if
# # multiple elif 
# always need a condition like if statement

# score = 91
# if score >= 90:  #if true then jumps to end
#     print("A") 
# elif score >= 80:
#     print("B")
# else :
#     print("False")

# score = 80
# if score >= 90: #false
#     print("A") 
# elif score >= 80: #false
#     print("B")
# else :
#     print("False")


# #branchng elif elif
# #usecase like grading system, assigning roles to the users, working with code of status 

# score = 39
# if score >= 90: #false
#     print("A") 
# elif score >= 80: #false
#     print("B")
# elif score >= 60: #false
#     print("C")    
# elif score >= 40: #false
#     print("D")
# elif score >= 33: #false
#     print("E")
# else :
#     print("Fail")