

# ############################################ Practice Questions ##################################################################

# ##################################################################################################################################
# ############################################################# Claude #############################################################

# # # 20 practise question (easy question)

# ##################################################################################################################################

# # E1
# # for loop
# # Print numbers 1 to 20
# # Print all numbers from 1 to 20 each on a new line.

# for i in range(1,21):
#     print(i)

# ##################################################################################################################################

# # E2
# # for loop
# # Print squares of numbers
# # Print the square of every number from 1 to 10. Output: 1, 4, 9, 16 ...

# square = 0
# for i in range(1,11):
#     print(i * i)

# ##################################################################################################################################

# # E3
# # while loop
# # Print numbers while less than 50
# # Start from 1. Use a while loop to print numbers as long as they are less than 50.

# i = 1
# while i < 50:
#     print(i)
#     i = i + 1
    
# ##################################################################################################################################

# # E4
# # for loop
# # Sum of odd numbers
# # Find and print the sum of all odd numbers from 1 to 50.

# sum = 0
# for i in range(1,51):
#     if i % 2 == 1:
#         sum = sum + i
# print(sum)

# ##################################################################################################################################

# # E5
# # for loop
# # Print multiples of 7
# # Print all multiples of 7 from 7 to 70.

# for i in range(1,71):
#     if i % 7 == 0 :
#         print(i)

# ##################################################################################################################################

# # E6
# # while loop
# # Triple until over 500
# # Start with n=1. Keep tripling it and printing until it exceeds 500.

# n = 1
# while n < 500:
#     print(n)
#     n = n * 3
    
# ##################################################################################################################################

# # E7
# # for loop
# # Count characters in a word
# # Ask user for a word. Count total characters in it using a loop (don't use len()).

# word = input("word:")
# n = 0
# for i in word:
#     n = n + 1
# print(n)

# ##################################################################################################################################

# # E8
# # for loop
# # Print numbers in reverse
# # Print numbers from 20 down to 1 using a for loop.

# for i in range(20, 0, -1):
#     print(i)

# ##################################################################################################################################

# # E9
# # while loop
# # Ask until positive number
# # Keep asking the user to enter a positive number. If they enter 0 or negative, ask again. Stop when they give a positive number.

# while True:
#     User = int(input("number: "))
#     if User <= 0:
#         print("must be positve number, try again")
#     else:
#         print("postive number, thanks")
#         break

# ##################################################################################################################################

# # E10
# # for loop
# # Print even numbers in reverse
# # Print all even numbers from 20 down to 2.

# for i in range(20,0,-1):
#     if i % 2 == 0:
#         print(i)

# ##################################################################################################################################

# # E11
# # for loop
# # Product of numbers 1 to 10
# # Multiply all numbers from 1 to 10 together and print the result (it's 3628800).

# multi = 1
# for i in range(1,11):
#     multi = multi * i
# print(multi)

# ##################################################################################################################################

# # E12
# # for loop
# # Print only consonants
# # Ask for a word. Print only the consonants (non-vowel letters) one by one.

# word = input("word: ").lower()
# for i in word:
#     if i not in "aeiou":
#         print(i)

# ##################################################################################################################################

# # E13
# # while loop
# # Sum numbers until enters 0
# # Keep asking the user to enter a number. Add each to a running total. Stop when they enter 0 and print the total.
    
# total = 0
# while True:
#     user = int(input("Number: "))
#     if user == 0:
#         break
#     total = user + total
#     print(total)

# ##################################################################################################################################

# # E14
# # for loop
# # Print number and its cube
# # For numbers 1 to 5, print each number and its cube. Like: 2 cubed = 8

# for i in range(1,6):
#     cube = i * i * i
#     print(f"{i} : {cube}")

# ##################################################################################################################################

# # E15
# # for loop
# # Count down by 5
# # Print numbers from 100 down to 0 counting by 5 each time.

# for i in range(100,-1,-5):
#     print(i)

# ##################################################################################################################################

# # E16
# # for loop
# # Check if word has letter 'a'
# # Ask user for a word. Use a loop to check if it contains the letter 'a'. Print yes or no.

# user = input("word: ")
# found = False
# for i in user:
#     if i == "a" :
#         found = True
#         break
# if found:
#         print("yes contains a")

# else:
#     print("no a in word")

# ##################################################################################################################################

# # E17
# # while loop
# # Average of 5 numbers
# # Ask the user to enter exactly 5 numbers one by one. Print their average at the end.

# total = 0
# for i in range(1,6):
#     user = int(input("num: "))
#     total += user
# print(total/5)

# ##################################################################################################################################

# # E18
# # for loop
# # Print index and character
# # Ask user for a word. Print each character with its index. Like: 0 → p, 1 → y ...

# word = input("word: ")
# count = -1
# for i in word:
#     count += 1
#     print(f"{count} -> {i}")
# # or
# word = input("word: ")
# for i in range(len(word)):
#     print(i, "->", word[i])

# ##################################################################################################################################

# # E19
# # for loop
# # Print numbers not divisible by 4
# # Print all numbers from 1 to 40 that are NOT divisible by 4.

# for i in range(1,41):
#     if i % 4 !=0:
#         print(i)

# ##################################################################################################################################

# # E20
# # while loop
# # Repeat until correct answer
# # Ask the user "What is 8 x 7?" repeatedly until they answer 56 correctly. Then print "Correct!"

# while True:
#     user = int(input("8 * 7 is: "))
#     if user == 56:
#         print("correct!")
#         break

# ##################################################################################################################################

# ##################################################################################################################################


