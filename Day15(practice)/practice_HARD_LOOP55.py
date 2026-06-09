# ############################################################# Claude ############################################################

# # #  practise question (20 hard)

# ##################################################################################################################################

# # H1
# # nested loops
# # Diamond pattern
# # Print a diamond shape of stars with width 5 at center:
# #   *
# #  ***
# # *****
# #  ***
# #   *

# n = 5
# for i in range(3):
#     for j in range(i+1,3):
#         print(" ", end="")
#     for j in range(i+1):
#         print("*", end="")
#     for j in range(i):
#         print("*", end="")
#     print()
# for i in range(2):
#     for j in range(i+1):
#         print(" ", end="")
#     for j in range(i,2):
#         print("*", end="")
#     for j in range(i+1,2):
#         print("*", end="")
#     print()



# n = 5
# for i in range(1, n+1, 2):        # runs 1,3,5
#     print(" " * ((n-i)//2) + "*" * i + " " * ((n-i)//2))
# for j in range(n-2, 0, -2):       # runs 3,1
#     print(" " * ((n-j)//2) + "*" * j + " " * ((n-j)//2))


# #################################################################################################################################


# # H2
# # while + logic
# # GCD using Euclidean algorithm
# # Ask user for two numbers. Find their GCD (Greatest Common Divisor) using a while loop and the Euclidean algorithm.

# a = int(input("enter no: "))
# b = int(input("enter no: "))
# while b != 0:
#     a, b = b , a % b
# print(a)


# #################################################################################################################################

    
# # H3
# # nested + logic
# # Multiplication table grid
# # Print a formatted 5x5 multiplication grid with row and column headers. Numbers aligned neatly.

# print(" ", end="")
# for i in range(1, 6):
#     print(f"{i:4}", end="")
# print()
# for i in range(1,6):
#     print(f"{i:4}", end="")
#     for j in range(1,6):
#         print(f"{i*j:4}", end="")
#     print()

# print(" ", end="")
# for i in range(1, 6):
#     print(f"{i:4}", end="")
# print()
# for i in range(1, 6):
#     print(f"{i:4}", end="")
#     for j in range(1, 6):
#         print(f"{i*j:4}", end="")
#     print()


# #################################################################################################################################


# # H4
# # while + logic
# # Binary to decimal
# # Ask user to enter a binary number (e.g. 1010). Convert it to decimal using a loop without using int(n, 2).

# binary = input("Enter binary: ")
# decimal = 0
# for bit in binary:
#     decimal = decimal * 2 + int(bit)
# print("Decimal: ", decimal)


# #################################################################################################################################


# # H5
# # for + logic
# # Pascal's triangle
# # Print the first 6 rows of Pascal's triangle using loops.

# row = [1]
# for i in range(6):
#     print(row)
#     new_row = [1]
#     for j in range(len(row)-1):
#         new_row.append(row[j] + row[j+1])
#     new_row.append(1)
#     row = new_row


# #################################################################################################################################


# # H6
# # while + full logic
# # Simple number menu
# # Build a menu that loops: 1) Check prime 2) Check palindrome 3) Factorial 4) Quit. Keep showing menu until user picks 4.

# while True:
#     print("1. prime, 2. palindrome, 3. factorial, 4. quit")
#     choice = input("choice: ")
#     if choice == "1":
#         flag = True
#         number = int(input("enter a number: "))
#         for i in range(2,number):
#             if number % i == 0:
#                 flag = False
#                 break
#         if flag:
#             print("prime")    
#         else:
#             print("not prime")
#     if choice == "2":
#         word = input("Word: ")
#         newword = ""
#         for i in word:
#             newword = i + newword
#         if newword == word:
#             print("palindrome")
#         else:
#             print("not palindrome")
#     if choice == "3":
#         factorial = 1
#         number = int(input("enter a number: "))
#         for i in range(1, number + 1):
#             factorial = factorial * i
#         print (factorial)
#     if choice == "4":
#         print("quit")
#         break


# w = input("Word: ")
# print("Palindrome" if w == w[::-1] else "Not palindrome")


# #################################################################################################################################


# # H7
# # for + logic
# # Find all divisors
# # Ask user for a number. Print all its divisors and count them. Also print if the number is prime.

# number = int(input("enter a number: "))
# count = 0
# for i in range(1, number + 1):
#     if number % i == 0:
#         print(i)
#         count += 1
# if count == 2:
#     print("is prime")
# else:
#     print("not prime")
# print(count)
    

# #################################################################################################################################


# # H8
# # while + logic
# # Digital root
# # Ask user for a number. Keep summing its digits until you get a single digit. E.g. 9875 → 9+8+7+5=29 → 2+9=11 → 1+1=2

# number = int(input("enter a number: "))
# while number > 10:
#     total = 0
#     for i in str(number):
#         total = total + int(i)
#     number = total
# print(number)


# #################################################################################################################################
# # H9
# # nested + pattern
# # Number diamond
# # Print this number diamond:
# #   1
# #  121
# # 12321
# #  121
# #   1

# n = 3
# for i in range(1,n+1):
#     print(" " * (n-i), end= "")
#     for j in range(1,i+1):
#         print(j, end="")
#     for j in range(i-1, 0 ,-1):
#         print(j, end="")
#     print()
# for i in range(n-1,0,-1):
#     print(" " * (n-i), end="")
#     for j in range(1, i+1):
#         print(j, end="")
#     for j in range(i-1, 0 ,-1):
#         print(j, end="")
#     print()

    
# #################################################################################################################################


# # H10
# # while + logic
# # Sieve of Eratosthenes
# # Find all primes up to 100 using the Sieve of Eratosthenes method with loops.

# sieve = [True] * 101
# sieve[0] = sieve[1] = False
# for i in range(2,11):
#     if sieve[i]:
#          for j in range(i * i, 100 + 1, i):
#             sieve[j] = False
# print("Prime numbers up to 100:")
# for num in range(2, 100 + 1):
#     if sieve[num]:
#         print(num, end=" ")
# print()

# sieve = [True] * 101
# sieve[0] = sieve[1] = False
# for i in range(2, 101):
#     if sieve[i]:
#         for j in range(i*2, 101, i):
#             sieve[j] = False
# for i in range(101):
#     if sieve[i]:
#         print(i, end=" ")

# #################################################################################################################################


# # H11
# # for + string
# # Caesar cipher encoder
# # Ask user for a message and a shift number. Encode it by shifting each letter by that many positions in the alphabet. E.g. "abc" shift 2 → "cde".




# #################################################################################################################################


# # H12
# # while + full logic
# # Simple bank account
# # Start with balance=1000. Loop showing menu: 1) Deposit 2) Withdraw 3) Balance 4) Exit. Prevent withdrawing more than balance.

# balance = 1000
# while True:
#     print("1. Deposit 2. Withdraw 3. Balance 4. Exit")
#     choice = input("Choice: ")
#     if choice == "1":
#         Deposit = int(input("Deposit amount: "))
#         balance = balance + Deposit
#         print("total balance: ", balance)
#         break
#     elif choice == "2":
#         withdraw = int(input("Withdraw: "))
#         if withdraw > balance:
#             print("Insufficeint balance: ")
#         else:
#             balance = balance - withdraw
#             print("balance: ", balance)
#         break
#     elif choice == "3":
#         print("balance: ",balance)
#         break
#     elif choice == "4":
#         print("Thankyou for banking with us")
#         break


# #################################################################################################################################


# # H13
# # for + logic
# # Find LCM
# # Ask user for two numbers. Find their LCM (Least Common Multiple) using a loop.

# a = int(input("enter a no: "))
# b = int(input("enter a no: "))
# n = a * b
# for i in range(1, n+1):
#     if i % a == 0 and i % b == 0:
#         print(i)



# #################################################################################################################################


# # H14
# # for + logic
# # Anagram checker
# # Ask user for two words. Check if they are anagrams of each other (same letters, different order) using loops only — no sort().

# word1 = input("enter word 1: ").lower()
# word2 = input("enter word 2: ").lower()

# if len(word1) != len(word2):
#     print("not a anagram")
# else:
#     for i in word1:
#         if word1.count(i) != word2.count(i):
#             print("not a anagram")
#             break
#     else:
#         print("anagram")


# #################################################################################################################################


# # H15
# # while + full logic
# # Word guessing game
# # Set a secret word. Show blanks (_) for each letter. User guesses one letter at a time. Reveal correct letters. Give 6 wrong guess limit. Print win or lose.

# secret = "modric"

# #################################################################################################################################


# # H16
# # nested loop
# # Print a number pyramid
# # Print this pattern for 5 rows:
# # 1
# # 1 2
# # 1 2 3
# # 1 2 3 4
# # 1 2 3 4 5

# n = 5
# for i in range(1, n+1):
#     for j in range(1,i+1):
#         print(j, end = "")
#     print()


# #################################################################################################################################


# # H17
# # while + logic
# # Collatz conjecture
# # Ask for a number n. If it is even, divide by 2. If odd, multiply by 3 and add 1. Repeat until n reaches 1. Print each step and count how many steps it took.

# n = int(input("Enter a number: "))
# count = 0
# while n != 1:
#     if n % 2 == 0:
#         n = n / 2
#     elif n % 2 != 0:
#         n = (n * 3) + 1
#     count += 1
#     print(n)
# print(count)


# #################################################################################################################################


# # H18
# # for + logic
# # Fibonacci sequence
# # Print the first 15 numbers of the Fibonacci sequence (0, 1, 1, 2, 3, 5, 8...) using a loop.

# a = 0
# b = 1
# n = 15
# for i in range(0,n+1):
#     print(a)
#     a, b = b, a + b

# a = 0
# b = 1
# n = 15
# temp = 0
# for i in range(0,n+1):
#     print(a)
#     temp = a
#     a = b
#     b = temp + b


# #################################################################################################################################


# # H19
# # while +full logic
# # Mini calculator loop
# # Build a calculator that keeps running. Each round ask the user for two numbers and an operator (+, -, *, /). Show the result. 
# # If the user types "quit" as the operator, stop the program  

# while True:
#     num1 = int(input("enter no1: "))
#     num2 = int(input("enter no2: "))
#     operator = input(" enter operator: ")
#     if operator == "+":
#         sum = num1 + num2
#         print(sum)
#     elif operator == "-":
#         sub = num1 + num2
#         print(sub)
#     elif operator == "*":
#         multi = num1 * num2
#         print(multi)
#     elif operator == "/":
#         div = num1 / num2
#         print(div)
#     elif operator == "quit":
#         break


# #################################################################################################################################


# # H20
# # nested loops
# # print star pattern 
# # *****
# #  ***
# #   *
# #  ***
# # *****

# for i in range(3):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(i,3):
#         print("*", end="")
#     for j in range(i+1,3):
#         print("*", end="")
#     print()
# for i in range(1,3):
#     for j in range(i+1,3):
#         print(" ", end="")
#     for j in range(i+1):
#         print("*", end="")
#     for j in range(i):
#         print("*", end="")
#     print()


# #################################################################################################################################