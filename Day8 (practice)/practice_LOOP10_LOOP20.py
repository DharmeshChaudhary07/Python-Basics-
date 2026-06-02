
########################################### Practice Questions ############################################################


# A for loop in Python iterates over each item in a sequence (e.g., list, tuple, or string).
#  It checks if the "last item" in the sequence has been reached; 
# if not, it assigns the next item to a variable and executes the loop body

# while loop checks a condition before each iteration. If the condition is True, 
# the code inside the loop executes,
#  and then the condition is checked again. If it is False, the loop terminates.


########################################################### Claude ###########################################################

# 10 practise question (4 easy, 4 medium and 2 hard)

###############################################################################################################################


# Print 1 to 10 # # Print all numbers from 1 to 10, each on a new line using a for loop.

for i in range(1,11):
    print(i)

###############################################################################################################################

# Sum of 1 to 100 # # Calculate and print the sum of all numbers from 1 to 100 using a for loop.

total = 0
for i in range(1,101):
    total = i + total
print(total)

###############################################################################################################################

# Countdown from 10 # # Print a countdown from 10 down to 1 using a while loop. Print "Go!" at the end.

n = 10
while n >= 1:
    print(n)
    n = n - 1
print("Go!")

###############################################################################################################################

# Multiplication table of 5 # # Print the multiplication table of 5 from 5×1 to 5×10. Each line: 5 x 1 = 5

table = 5
for i in range(1,11):
    total = 5 * i
    print(f'5 * {i} = {total}')

###############################################################################################################################

# Print even numbers # # Print only the even numbers between 1 and 20. Use a for loop with an if condition inside.

for i in range(1,21):
    if i % 2 == 0:
        print(i)

###############################################################################################################################

# Print numbers 1 to 30. Print "Fizz" for multiples of 3, "Buzz" for multiples of 5, "FizzBuzz" for multiples of both — otherwise print the number.

for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

###############################################################################################################################

#Number guessing game # #Set secret = 7. Keep asking the user to guess a number. Print "Try again" until they get it right, then print "Correct!" and stop.

sceret = 7
while True:
    guess = int(input("Guess: "))
    if guess == sceret:
        print ("Correct !")
        break    
    else :
        print("Try again")
        
###############################################################################################################################        

# Skip multiples of 3 # # Print numbers 1 to 20, but skip any number that is a multiple of 3. Use the continue keyword.

for i in range(1,21):
    if i % 3 == 0:
        continue
    print(i)

###############################################################################################################################

# Factorial calculator # Ask the user for a number n, then calculate its factorial using a while loop. Factorial of 5 = 5×4×3×2×1 = 120.

total = 1
n = int(input("Enter a number: "))
while n >= 1:
    total = n * total
    n -= 1
print(total)
    
###############################################################################################################################

# Star pattern # # Print this pattern using loops:
# *
# **
# ***
# ****
# *****

for i in range(1,6):
    print(i * "*")



#################################################################################################################################
############################################################ Claude #############################################################

# 16 extra practise question (8 easy and 8 medium)

#################################################################################################################################
#################################################################################################################################

# Print odd numbers # # Print all odd numbers from 1 to 15.

for i in range(1,16):
    if i % 2 == 1:
        print(i)

###############################################################################################################################

# Print each character of a string # # Ask the user for their name. Print each character on a new line using a for loop.

name = input("Your goodname? ")
for i in name:
    print(i)

###############################################################################################################################

# Double until over 100 # # Start with n = 1. Keep doubling it using a while loop and print each value until it exceeds 100.

n = 1
while n <= 100:
    print(n)
    n = n * 2
    
###############################################################################################################################

# Sum of even numbers # # Find and print the sum of all even numbers from 1 to 50.

sum = 0
for i in range(1,51):
    if i % 2 == 0:
        sum = i + sum
print(sum)

###############################################################################################################################

# Repeat a word # Ask the user for a word and a number n. Print that word n times using a for loop.

word = input("Word: ")
number = int(input("number: "))
for n in range(number):
    print(word)

###############################################################################################################################

# Keep asking until "quit" # # Keep asking the user to enter something. Stop the loop only when they type "quit".

while True:
    enter = input("enter something: ")
    if enter == "quit":
        break 

###############################################################################################################################

# Count down by 3 # # Print numbers from 30 down to 0, counting down by 3 each time (30, 27, 24 ... 0).

for i in range(30,-1,-3):
    print(i) 

###############################################################################################################################

# Count vowels in a word # # Ask the user for a word. Count and print how many vowels (a, e, i, o, u) it contains.

word = input("enter a word: ")
count = 0
for i in word:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        count = count+1
print(count)
    
###############################################################################################################################

# Prime number check # Ask the user for a number. Check if it is prime (divisible only by 1 and itself) and print the result.

number = int(input("enter a number: "))
numberisprime = True
for i in range(2,number):
    if number % i == 0:
        numberisprime = False
        break
if numberisprime and number > 1:
    print(number,"is prime")
else:
    print(number, "not prime")

###############################################################################################################################

 # Safe number input # Keep asking the user to enter a number. If they type something that is not a number, print "Invalid! Try again" and ask again. Stop when they give a valid number.

while True:
    try:
        n = int(input("Enter a number: "))
        break
    except:
        print("invalid! try again")

###############################################################################################################################

# Find the largest number # Ask the user to enter 5 numbers one by one using a loop. After all 5 are entered, print the largest one.

largest = None
for i in range(5):
    n = int(input("Enter a number: "))
    if largest is None or n > largest:
        largest = n
        print("largest:" ,largest)

###############################################################################################################################

# Reverse a string # Ask the user for a word. Print it in reverse using a loop (do not use slicing).

result = ""
word = input("enter a word: ")
for i in range(len(word)-1, -1, -1):
        result += word[i]
print(result)

result = ""
word = input("enter a word: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])

###############################################################################################################################

# Login with 3 attempts# Set a password = "python123". Give the user 3 attempts to guess it. Print "Access granted" or "Locked out" based on the result.

password = "python123"
n = 0
while n < 3:
    userpass = input("enter a password:") 
    if userpass == password:
        print("Access granted")
        break
    n += 1
else: 
    print("Locked out")

###############################################################################################################################

# Count positive and negative # Ask the user to enter 6 numbers. Count how many are positive and how many are negative. Print both counts at the end.

pos = 0
neg = 0
for i in range(6):
    number = int(input("Enter no: "))
    if number < 0:
        neg = neg + 1
    elif number > 0:
        pos = pos + 1
print(pos, neg)

###############################################################################################################################
    
# All multiplication tables # Print multiplication tables for numbers 1 through 5. Each table goes from x×1 to x×10.

for i in range(1,6):
    print(f'-----table of {i}----')
    for j in range(1,11):
        sum = i * j
        print(f'{i} * {j} = {sum}')

###############################################################################################################################

# Skip numbers divisible by both 2 and 3 # Print numbers 1 to 30 but skip any number divisible by both 2 and 3 (i.e. 6, 12, 18...). Use continue.

for i in range(1,31):
    if i % 2 == 0 and i % 3 == 0:
        continue
    print(i)

###############################################################################################################################
