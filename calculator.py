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
# [] separate funtions for operations
# [] add testing 
# [] finalise intro text, remove test statements from intro
# [] make the calculator run without closing until a command for closing the programm is given
# [] add more error and input handling: letters, other input mistakes and handle negative numbers

# Input criteria
# -> one line / one input
# -> start with 2 numbers 
# -> 1 operation

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

    print(x, y, requested_operation)

    return x, y, requested_operation

#TO DO: create separate functions for operations -> ease of testing; then add them to calculator main with if conditions
def calculate(x, y, requested_operation): 
    result = 0

    if requested_operation == "+":
        result = x + y
    elif requested_operation == "-":
        result = x - y
    elif requested_operation == "*":
        result = x * y
    elif requested_operation == "/":
        result = x / y

    print("%.2f -> first number \n%.2f -> second number \n%s \t-> operation to perform \n----------\nRESULT: %.2f" %(x, y, requested_operation, result))
    return result

def calculator_main():
    welcome_message = "Welcome to the calculator. \n----------\nPossible operations: \naddition \t-> + \nsubtraction \t-> - \nmultiplication \t-> * \ndivision \t-> / \n----------\nQUIT: q"
    print(welcome_message)
    user_input = input("Calculate:").replace(" ", "")

    if user_input == "Q" or user_input == "q":
        return
    else: 

        try: 
            calculate(*convert(user_input))

        except: 
            print("Cannot calculate, invalid input. Try again.")

calculator_main()