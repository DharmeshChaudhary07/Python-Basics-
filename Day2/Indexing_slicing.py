# ################ Data extraction : indexing and slicing ##################

# # "hello" : python think it is a sequence of characters
# #each character has postion - called index
# #two index -> positive and negative index
# #slicing -> to return the group of characters

# #slicing and indexes
# #extracts the text 
# text = "dharmesh"
# print(text[2])
# print(text[-3])
# print(text[0:4])  
# print(text[2:])
# print(text[:5])
# print(text[0:7])
# print(text[-6:-2])
# print(text[0:8:1])
# print(text[0:8:2])

# #extracts the dates
# text = "26-03-2012"
# print(text[2])
# print(text[-3])
# print(text[0:4])  
# print(text[2:])
# print(text[:3])
# print(text[0:7])
# print(text[-6:-2])
# print(text[0:8:1])
# print(text[0:8:2])

######################### cleainig the string ##################################
#lstrip(), rstrip(), strip() {cleaning the white space in the data}

# text = "Engineering"
# print(text)
# text = " Engineering".lstrip()
# print(text)
# text = "Engineering ".rstrip()
# print(text)
# text = " Engineering " .strip()
# print(text)
# text = "Engineering               " .strip()
# print(text)

# #we never know where the user might add the spaces, better use strip() to remove all the space from both ends.
# # doesnt remove spaces from the middle

# #if there is no space but some special characters in left or right side of text just declare it in the strip function eg. strip("@#$$").

text = "#Engineering#####".strip("#")
print(text)
text = "$$$$$$#Engineering#####$$$".strip("#$")
print(text)

# #Use case *(how do we check for spaces at the start or end without looking at the data)
# #detect extra space -> check the length before and after strip to find unwanted spaces

# text = "     engineering  "
# print(len(text))
# print(len(text.strip()))
# print(len(text) == len(text.strip()))
# print(len(text) - len(text.strip()))

# text = "  dharmesh chaudhary     "
# print(text.strip())

##### example ####
# text = " University of new south wales       "
# print(text.strip())
# print(len(text))
# print(len(text.strip()))
# no_of_space = len(text)- len(text.strip())
# is_clean = len(text) == len(text.strip())
# print("Num of space:" , no_of_space)
# print("Data is clean:", is_clean)
