def add(a, b):       # function add
    return a + b

def subtract(a, b):   # function sub
    return a - b

def multiply(a, b):    # function multiply
    return a * b

def divide(a, b):       # function divide
    if b == 0:          # can not be zero
        return "Error: division by zero"
    return a / b

# def calculator(a, op, b):
#     if op == '+':
#         result = add(a, b)
#     elif op == '-':
#         result = subtract(a, b)
#     elif op == '*':
#         result = multiply(a, b)
#     elif op == '/':
#         result = divide(a, b)
#     else:
#         return f"Unknown operator '{op}'"

#     if isinstance(result, float) and result.is_integer():
#         result = int(result)

#     return result

# print(calculator(10, '+', 5))   # 15
# print(calculator(100, '/', 4))  # 25
# print(calculator(6, '*', 7))    # 42
# # print(calculator(10, '/', 0))   # Error: division by zero

def calculator():      # main function
    print("=== Python Calculator ===")   # intro 
    print("Operations: +  -  *  /")      # intro
    print("Type 'quit' to exit\n")       # intro

    while True:        # Because you don't know in advance how many calculations the user wants to do:
        try:
            user_input = input("Enter expression (e.g. 10 + 5): ")    # user input
            user_input = user_input.strip()      # remove extra space 

            if user_input.lower() == 'quit':   # if user used 'quit'
                print("Bye!")
                break                          # exit the loop 

            # split input into: number operator number
            parts = user_input.split()          # split "10 + 5" into and convert it into a ['10', '+', '5']
            if len(parts) != 3:                 # # check if we got exactly 3 parts
                print("Invalid input. Use format: number operator number\n")  
                continue    # jump straight back to top of loop  ← skips everything below


            a = float(parts[0])                       # convert first part '10' to number 10.0
            op = parts[1]                             # take the operator '+', '-', '*' or '/'
            b = float(parts[2])                       # convert third part '5' to number 5.0

            if op == '+':
                result = add(a, b)          # call add function
            elif op == '-':
                result = subtract(a, b)     # call sub function
            elif op == '*':
                result = multiply(a, b)     # call multiply function
            elif op == '/':
                result = divide(a, b)       # call divide function
            else:
                print(f"Unknown operator '{op}'. Use +  -  *  /\n")
                continue                   # skip rest of loop and ask again

            # show clean int if no decimal needed
            if isinstance(result, float) and result.is_integer():   # is the result a float? (not a string like "Error: division by zero") and # is the float a whole number? e.g. 25.0 → yes, 25.6 → no
                result = int(result)            # if both isinstance and is_integer is true -> convert it to integer

            print(f"= {result}\n")     # always run 

        except ValueError:
            print("Invalid number. Try again.\n")

calculator()                # call main function 