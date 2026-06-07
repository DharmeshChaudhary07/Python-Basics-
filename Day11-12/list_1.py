
############################################################################################################################################################################################

# Operation we can do we list:

########################################################################################################################################################################


                                             # Changing list (.append(), insert(), remove(), clear(), pop(), update)

############ Add item to list ############ 

# .append() - Adds the item to the end of the list.

letter = ['a', 'b', 'c', 'd']
letter.append('x')
letter.append('y')
print(letter)

########### insert() ############ 
# insert at specific postion

letter = ['a', 'b', 'c', 'd']
letter.insert(2, 'x')
letter.insert(4,'y')
print(letter)


matrix = [[1,2,3],  
          [4,5,6],   
           [7,8,9]]
matrix.append(['x', 'y', 'z'])
matrix.insert(1, ['x', 'y', 'z'])
matrix[1].append('x')      # add only at the end 
matrix[0].insert(2, 'y')
print(matrix)



########### Remove item ############ 

# clear() - removes all the item in the list 
# remove() - remove only the first match in the list (by value)

letter = ['a', 'b', 'c', 'a']
letter.clear()     # prints []           
letter.remove('b')           # removing by value only first match 
letter.remove("a")

########### Pop item ############ 

# pop() remove the item by positon (by position)
# it removes and returns an item.

letter = ['a', 'b', 'c', 'a']
letter.pop(0)   # remove from index 0
letter.pop()   # remove the last item
removed = letter.pop()
removed = letter.pop(2)
print(letter)              # print the list - ['a', 'b', 'c']
print("Removed Item:", removed)         # print 'a' return the value removed.

matrix = [[1,2,3],  
          [4,5,6],   
           [7,8,9]]
matrix.remove([1,2,3])
matrix.pop()
matrix[1].remove(5)
matrix[1].pop(1)
matrix[0].pop(0)
print(matrix)

############ Update item ############ 

letter[3]= 'd'    # prints ['a', 'b', 'c', 'd']
letter = 'z'      # print z removes the whole list
print(letter)
print(type(letter))  # from list to str

matrix[2] = ['a', 'b', 'c']
matrix[0][2] = '-' 
matrix[1][1] = '-' 
matrix[2][0] = '-' 
print(matrix) 


########################################################################################################################################################################


                                             # order data (sort,  sort(reverse = True),  sorted, reverse(), reversed )

########### sort by price, sort name alphabetical ############


letter = ['a', 'd', 'b', 'c']        
letter.sort()                     # print ['a', 'b', 'c', 'd']         
letter.sort(reverse=True)       
print(letter)

matrix = [[2,3,3],        # compares the only first by item  
          [1,2,9],
             [1,1,6]]
matrix.sort()     # prints [[1, 1, 6], [1, 2, 9], [1, 3, 3]]
print(matrix)

########### sorted() ############
#  The sorted() function returns a new sorted list from any iterable, without modifying the original.
# syntax sorted(iterable, *, key=None, reverse=False)

newlist = sorted(letter , reverse= True)
print("orignal list:" , letter)
print("sorted list:" , newlist)

########### .reverse() - just flip around the list ############
letter.reverse()
newlist =  list(reversed(letter))            # reversed creates an iterator object, not a list: use list (convert iterator -> list)
print("original list:" , letter)
print("New list:" , newlist)


########################################################################################################################################################################


                                             # copy data (assignment = , .copy() also called (shallow copy), copy and deepcopy library)

# copy and make duplicate list to work on. original list unchanged.

letter = ['a', 'd', 'b', 'c']  

########### copying list (assignment = ) ############

# eg. orignal = ['a', 'b', 'c'] 
#     copylist = orginal      # # it won't copy, its just a reference to orginal list.

lettercopy = letter
lettercopy.append('e')
print(letter)          # change both list (orignal and copylist)
print(lettercopy) 


########### coping list .copy() ############
# simple list has only one level — no children, so nothing is shared

lettercopy = letter.copy()
lettercopy.append('e')
print(letter)      
print(lettercopy) 
lettercopy.remove('a')
print(lettercopy)

# Matrix has two levels — children are shared.
# shallow copy creates a new parent, but the children are shared (same memory) Changing a child affects both because they point to the same inner list.

matrix = [[1,2,3],  
          [4,5,6],   
           [7,8,9]]
matrixcopy = matrix.copy()
matrixcopy[1].append('x')
print(matrix)
print(matrixcopy)
# prints : [[1, 2, 3], [4, 5, 6, 'x'], [7, 8, 9]]
#.         [[1, 2, 3], [4, 5, 6, 'x'], [7, 8, 9]]


########### coping list copy and deepcopy ############ 

# library - import copy deepcopy
# copy creates a new parent, but the children are shared (same memory): Changing a child affects both because they point to the same inner list.
# deepcopy() creates a true, independent copy for all level

import copy
matrixcopy = copy.copy(matrix)   # it works just like shallow copy .copy() no change at child prints [[1, 2, 3], [4, 5, 6, 'x'], [7, 8, 9]] \n [[1, 2, 3], [4, 5, 6, 'x'], [7, 8, 9]]
# matrixcopy = copy.deepcopy(matrix)    # prints # # prints [[1, 2, 3], [4, 5, 6], [7, 8, 9]] \n [[1, 2, 3], [4, 5, 6, 'x'], [7, 8, 9]]
matrix.pop()
matrixcopy[1].append('x')
print(matrix)
print(matrixcopy)


######## testing is operator in copy ########

import copy
matrix = [[1,2,3],  
          [4,5,6],   
           [7,8,9]]

# assignment
copy1 = matrix
print("same object?:" , matrix is copy1)   # pointing at same object in memory

# shallowcopy
copy2 = matrix.copy()   
# copy2 = copy.copy(matrix) 
print("same object?:" , matrix is copy2)          # prints false 
print("same object?:" , matrix[0] is copy2[0])    # sharing child - prints true

# # deepcopy
copy3 = copy.deepcopy(matrix)
print("same object?:" , matrix is copy3)
print("same object?:" , matrix[0] is copy3[0])    

# Tip; use is operator to check if the copies are truely indepedent.


########################################################################################################################################################################


                                             # Combining list

######### combining multiple list to one new list list ##########

letter =['a', 'b', 'c']
number = [1, 2, 3]
combinelist = letter + number
print(combinelist)
print(letter * 2) # mutliplier operator - makes copies of the same list in the same list

# combine but split into two list inside one list. [[]'a', 'b', 'c'], ['1', '2', '3']]
combinelist = [letter , number]     # print =[['a', 'b', 'c'], [1, 2, 3]]
print(combinelist) 

######### .extend() ###########
# #instead of making third list, we can add one list to another list. 
number.extend(letter)
print(number)
print(letter)

######### zip() ##########

#  Pair elements from multiple lists : output is list of tuple and will be iterator.

combinelist = zip(letter, number)
print(combinelist)   # print <zip object at 0x109e57e40>
combinelist = list(zip(letter, number))
print(combinelist)

number = [1, 2, 3, 4] 
combinelist = list(zip(letter, number))   # if the length is different in the list it will stop at shortest list.
combinelist = list(zip(letter, number, 'hi'))  # prints [('a', 1, 'h'), ('b', 2, 'i')]
print(combinelist)


##### eg. #######
 
id = [101, 102, 103]
name = ['rakhi', 'deepak', 'mamta']
# pair customer name with their IDs
print(list(zip(id, name)))