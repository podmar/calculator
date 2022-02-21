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
# [] add testing 
# [] finalise intro text, remove test statements from intro
# [] make the calculator run without closing until a command for closing the programm is given
# [] add more error and input handling

# Input criteria
# -> one line / one input
# -> start with 2 numbers 
# -> 1 operation

welcome_message = "Welcome to the calculator. \n----------\nPossible operations: \naddition \t-> + \nsubtraction \t-> - \nmultiplication \t-> * \ndivision \t-> / \n----------"

print(welcome_message)

user_input = input("Calculate:").replace(" ", "")

possible_operations = ["+", "-", "*", "/"]

requested_operation = ""

result = 0

x = 0
y = 0

for el in possible_operations: 
    operator_index = user_input.find(el)
    if operator_index > -1: 
        x = eval(user_input[0:operator_index])
        y = eval(user_input[operator_index+1:])
        requested_operation = el
        break

try: 
    if requested_operation == "+":
        result = x + y
    elif requested_operation == "-":
        result = x - y
    elif requested_operation == "*":
        result = x * y
    elif requested_operation == "/":
        result = x / y

    print("%.2f -> first number \n%.2f -> second number \n%s \t-> operation to perform \n----------\nRESULT: %.2f" %(x, y, requested_operation, result))

except: 
    print("Cannot calculate, invalid input. Try again.")
