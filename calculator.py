# REQUIREMENTS
# -> to be used in the command line
# -> operations: add, subtract, divide, multiply

# ACTION PLAN
# [x] decide on the input criteria
# [x] draft intro text
# [x] gather imput funtion(s)
# [x] eveluating / converting input
#       [x] choose which operation
#       [x] extract the numbers
# [x] making calculations
#       [] write calculation function(s)
#       [] call the right funtion
# [x] displaying result
# [] separate funtions for operations -> decided not to do, would complicate the logic: convert returns 3 arguments that are all needed by calculate
# [] add testing 
# [] finalise intro text, remove test statements from intro
# [] make the calculator run without closing until a command for closing the programm is given
# [] add more error and input handling: letters, other input mistakes and handle negative numbers

# Input criteria
# -> one line / one input
# -> start with 2 numbers 
# -> 1 operation

def instruction():
    welcome_message = "Welcome to the calculator. \n----------\nPossible operations: \naddition \t-> + \nsubtraction \t-> - \nmultiplication \t-> * \ndivision \t-> / \n----------\nQUIT: q"
    print(welcome_message)
    return

def convert(user_input):
    possible_operations = ["+", "-", "*", "/"]

    x = 0 
    y = 0
    requested_operation = ""

    for el in possible_operations: 
        operator_index = user_input.find(el)

        if operator_index > -1: 
            x = eval(user_input[0:operator_index])
            y = eval(user_input[operator_index+1:])
            requested_operation = el
            break

    return x, y, requested_operation

def calculate(x, y, requested_operation): 

    if requested_operation == "+":
        return add(x, y)
    elif requested_operation == "-":
        return subtract(x, y)
    elif requested_operation == "*":
        return multiply(x, y)
    elif requested_operation == "/":
        return divide(x, y)

    # print("%.2f -> first number \n%.2f -> second number \n%s \t-> operation to perform \n----------\nRESULT: %.2f" %(x, y, requested_operation, result))

def add(x, y): 
    result = 0
    result = x + y
    return result

def subtract(x, y): 
    result = 0
    result = x - y
    return result

def multiply(x, y): 
    result = 0
    result = x * y
    return result

def divide(x, y): 
    result = 0
    result = x / y
    return result

def calculator_main():

    user_input = input("Calculate:").replace(" ", "")

    if user_input == "Q" or user_input == "q":
        return False

    else: 

        try: 
            result = calculate(*convert(user_input))
            print("RESULT: %.2f" %(result))

        except: 
            print("Cannot calculate, invalid input. Try again.")
    

instruction() 

while True:
    calculator_main()

    if calculator_main() == False:
        break