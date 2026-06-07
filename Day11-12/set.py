
# ############################################################### Set ########################################################

# # used when we need to keep data unique.
# # unordered collection of unique value.
# # it store the data using hash function.
# # very fast - hash function

# my_set ={10,30,20,40 }
# print(my_set)    # print {40, 10, 20, 30}  # which mean set in unordered

# my_set ={10,30,20,10}
# print(my_set)     # {10, 20, 30}         #  no duplicates
# print(my_set[1])   # prints error         #  no indexing

# my_set.remove(30)
# print(my_set)       # prints {10,20}       # mutable 

# ####### methods in set #########

# # .add() - insert the item somewhere in the set, only if its new.
# my_set.add(40)
# print(my_set)    # prints {40, 10, 20, 30}



# # .update() - adds the value to the set (same like .append in list) but not at the end , adds anywhere
# my_set.update('hi')          # prints {10, 20, 'h', 'i', 30}
# # update() loops through the string character by character 'hi' → 'h', 'i' → adds each separately!
# # or shortcut 
# my_set |= {1.2,3,4,5,"hi"}     # print {1.2, 3, 4, 5, 10, 20, 'hi', 30} # shortcut to add multiple value at once.
# # Because |= merges set with set "hi" is already inside {} — so it's treated as one item, not iterated!
# print(my_set)



# # .remove() - removes the item if in the set, if value not in the set prints error.
# my_set.remove(30)
# print(my_set) 

# # if you give the value in remove which is not in the set it will show error - in that case use discard
# # .discard() - removes item if in the set, otherwise it doesnt do anything
# my_set.discard(30)
# print(my_set)

# ######### method to do comparision #########
# # .union(), .intersection(), .difference(), .symmetric_differnce()

# my_set ={10,30,20,70}
# my_set1 ={10,30,40,70}
# print(my_set.union(my_set1))                   # {70, 40, 10, 20, 30} - all unique value from both set
# print(my_set | my_set1)                        # same as union

# print(my_set.intersection(my_set1))            # {10, 70, 30} - returns only shared item

# print(my_set.difference(my_set1))              # {20}    - returns, only in a(my_set) not in b(my_set1)
# print(my_set1 - my_set)                        # {40}   - same as difference (here only in myset1 , not in my_set)

# print(my_set.symmetric_difference(my_set1))    # {40, 20} - returns, finds none shared value


# ######### set relationship methods ##########

# # .issubset() 
# print(my_set.issubset(my_set1))                  # prints false - if all item of a(my_set) exist in b(my_set1)

# # .issuperset()
# print(my_set.issuperset(my_set1))                # prints false - returns true when it includes all item of the other set

# # .isdisjoint()
# print(my_set.isdisjoint(my_set1))                # prints false - return true only if both set shares no item (No Overlapping)
