# ############################################################# Claude ############################################################

# # # 20 practise question (medium question)

# ##################################################################################################################################

# # M1
# # for + if
# # Print all primes up to 50
# # Print every prime number from 2 to 50

# for n in range(2,51):
#     flag = True
#     for i in range(2, n):
#         if n % i == 0:
#             flag = False
#             break
#     else:
#         print("is prime no: ",n)

# ##################################################################################################################################

# # M2
# # while + try/except
# # Safe division calculator
# # Ask user for two numbers and divide them. Handle both invalid input (non-number) and division by zero. Keep looping until successful.

# while True:
#     try:
#         a = float(input("numerator:"))
#         b = float(input("denominator:"))
#         print(a/b)
#         break
#     except ValueError:
#         print("valueError")
#     except ZeroDivisionError:
#         print("denominator cannot be 0")

# ##################################################################################################################################

# # M3
# # for + logic
# # Count digits in a number
# # Ask user for a number. Count how many digits it has using a loop (don't use len() or str()).

# n = int(input("Enter a number: "))
# count = 0
# while n > 0:
#     n //= 10
#     count += 1
# print("Digits:", count)


# ##################################################################################################################################

# # M4
# # for + if
# # Second largest number
# # Ask user to enter 6 numbers. Find and print the second largest number.

# largest = 0             # use float(-inf) for negative no
# second_largest = 0
# for i in range(6):
#     n = int(input("number: "))
#     if n > largest:
#         second_largest = largest
#         largest = n
#     elif n > second_largest:
#         second_largest = n
# print("second_largest: ",second_largest)


# ##################################################################################################################################

# # M5
# # for + string
# # Count words in a sentence
# # Ask user for a sentence. Count the number of words by counting spaces + 1 using a loop.

# sentence = input("sentence: ")
# count = 1
# for i in sentence:
#     if i == " ":
#         count += 1
# print("words count:", count)


# ##################################################################################################################################

# # M6
# # for + pattern
# # Inverted star pattern
# # Print this pattern:
# # *****
# # ****
# # ***
# # **
# # *

# for i in range(5,0,-1):
#     print("*" * i)

# ##################################################################################################################################

# # M7
# # while + counter
# # ATM PIN with 3 atnts
# # Set PIN=1234. Give user 3 atnts. After each wrong atnt show remaining tries. Print "Card blocked" if all fail.

# pin = 1234
# n = 0
# while n < 3:
#     user = int(input("PIN: "))
#     if user != pin:
#         print("atnts remaming: ", 3 - (n + 1))
#         n = n + 1
#         if n == 3:
#             print("Card blocked")
#     else:
#         print("granted")
#         break


# ##################################################################################################################################

# # M8
# # for + if
# # Grade calculator
# # Ask user to enter marks for 5 subjects. Calculate average and print grade: A(>=90), B(>=75), C(>=60), D(>=40), F(below 40).

# total = 0
# for i in range(5):
#     marks = float(input("marks of subjects: "))
#     total += marks
#     avg = total / 5
#     if avg >= 90:
#         grade = "A"
#     elif avg >= 75:
#         grade = "B"
#     elif avg >= 60:
#         grade = "C"
#     elif avg >= 40:
#         grade = "D"
#     else:
#         grade = "F"
# print(avg, grade)

# ##################################################################################################################################

# # M9
# # for + string
# # Check palindrome
# # Ask user for a word. Check if it reads the same forwards and backwards (palindrome) using a loop.

# user = str(input("Word: "))
# user1 = ""
# for char in user:
#     user1 = char + user1
# if user1 == user:
#     print("is palindrome")
# else:
#     print("not a palindrome")

# # or

# user = str(input("Word: "))
# user1 = ""
# for i in range(len(user)-1,-1,-1):    
#     user1 = user1 + user[i]
# if user1 == user:
#     print("is palindrome")
# else:
#     print("not a palindrome")

# ##################################################################################################################################

# # M10
# # for + if
# # Number to digits
# # Ask user for a number. Print each digit on a new line using a loop.

# user = int(input("enter a number: "))
# user = str(user)
# for i in user:
#     print(int(i))

# ##################################################################################################################################

# # M11
# # nested for
# # Box pattern
# # Print a 5x5 box of stars like:
# # *****
# # *****
# # *****
# # *****
# # *****

# for i in range(5):
#     for j in range(5):
#         print("*", end = "")
#     print()

# ##################################################################################################################################

# # M12
# # for + logic
# # Sum of digits
# # Ask user for a number. Find the sum of all its digits. (e.g. 1234 → 1+2+3+4 = 10)

# user = int(input("enter a number: "))
# user = str(user)
# total = 0
# for i in user:
#     i = int(i)
#     total += i
# print(total)

# ##################################################################################################################################

# # M13
# # while + logic
# # Guess higher or lower
# # Set secret=42. User guesses. Tell them "Too high" or "Too low" until correct. Count number of guesses.

# secret = 42
# count = 0
# while True:
#     user = int(input("guess a no: "))
#     count += 1
#     if secret > user:
#         print("too low")
#     elif secret < user:
#         print("too high")
#     else:
#         print("excellent guess")
#         break
#     print("No of guess : ", count)


# ##################################################################################################################################

# # M14
# # for + continue
# # Skip vowels in a sentence
# # Ask user for a sentence. Print it back with all vowels removed.

# sentence = input("sentence: ")
# for i in sentence:
#     if i in "aeiouAEIOU":
#         continue
#     print(i, end="")
# print()


# ##################################################################################################################################

# # M15
# # for + if
# # Count uppercase and lowercase
# # Ask user for a sentence. Count how many uppercase and lowercase letters it has.

# sentence = input("sentence: ")
# uppercase = 0
# lowercase = 0
# for i in sentence:
#     if i.isupper():
#         uppercase += 1
#     elif i.islower():
#         lowercase += 1 
# print(uppercase)
# print(lowercase)

# I am Dharmesh Chaudhary
# ##################################################################################################################################

# # M16
# # for + if
# # Perfect numbers up to 500
# # A perfect number equals the sum of its divisors (excluding itself). Print all perfect numbers up to 500. (6, 28, 496)


# for i in range(2,501):
#     total = 0
#     for j in range(1,i):
#         if i % j == 0:
#             total += j
#     if total == i:
#         print(i)



# ##################################################################################################################################

# # M17
# # for + string
# # Convert to uppercase manually
# # Ask user for a lowercase word. Convert it to uppercase without using .upper() — use ASCII values (ord/chr).

# user = input("word in lowercase: ")
# for i in user:
#     i = ord(i) - 32
#     print(chr(i), end="")
# print()



# ##################################################################################################################################

# # M18
# # while + logic
# # Number reversal
# # Ask user for a number. Reverse it using a while loop and math (not string methods). E.g. 1234 → 4321.

# user = int(input("Number: "))
# reverse = 0
# while user > 0:
#     digit = user % 10 
#     reverse = reverse * 10 + digit
#     user //= 10
# print(reverse)

# ##################################################################################################################################

# # M19
# # for + nested
# # Print hollow square
# # Print a 5x5 hollow square (stars only on border, spaces inside):
# # *****
# # *   *
# # *   *
# # *   *
# # *****

# for i in range(5):
#     for j in range(5):
#         if i == 0 or i == 4 or j == 4 or j == 0:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# ##################################################################################################################################

# # M20
# # for + logic
# # Armstrong number check
# # Ask user for a number. Check if it's an Armstrong number — each digit cubed and summed equals the number. (e.g. 153 = 1³+5³+3³)

# user = str(input("enter a no: "))
# total = 0
# for i in user:
#     i = int(i)
#     i = i ** 3
#     total += i
# if int(user) == total:
#     print("is a armstrong no")
# else:
#     print("not a armstrong no")
