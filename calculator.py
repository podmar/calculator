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
# [x] create separate funtions for operations -> not sure if that makes sense, the code is not simpler and the advantage for testing might be minor
# [x] add testing 
# [x] finalise intro text, remove test statements from intro
# [x] make the calculator run without closing until a command for closing the programm is given
# [x] add more error and input handling: letters, other input mistakes 
# [x] handle negative numbers
# [] check if possible to remove letters to fix the input (after or before eval)
# [] check possibility to rewrite simpler wiht compile /eval funtions only

# Input criteria
# -> one line / one input
# -> start with 2 numbers 
# -> 1 operation

import time

def instruction():
    welcome_message = "Welcome to the calculator. \n----------\nPossible operations: \naddition \t-> + \nsubtraction \t-> - \nmultiplication \t-> * \ndivision \t-> / \n----------\nQUIT: q\n----------"
    print(welcome_message)
    return

def convert(user_input):
    invalid_number_warning = "Please enter numbers."
    operator_warning = "You did not input a valid operator."
    possible_operations = ["+", "*", "/", "-"]

    requested_operation = ""

    def extracting_numbers(any_string_input, given_index): 
        try: 
            x = float(any_string_input[0:given_index])
            y = float(any_string_input[given_index+1:])
            
        except: 
            print(invalid_number_warning)
            x = None
            y = None

        numbers = [x, y]

        return numbers

    for el in possible_operations: 
        operator_index = user_input.find(el)

        if operator_index == -1: 
            continue

        elif operator_index > 0: 
            requested_operation = el

            converted_input = extracting_numbers(user_input, operator_index)

            break

        elif operator_index == 0: 
            requested_operation = el
            if requested_operation == possible_operations[3]: 
                operator_index = user_input[1:].find(el) + 1

                converted_input = extracting_numbers(user_input, operator_index)

                break

    if requested_operation == "": 
        print(operator_warning)
    
    converted_input.append(requested_operation)

    return converted_input

def calculate(x, y, requested_operation): 
    result = 0

    if requested_operation == "+":
        result = x + y
    elif requested_operation == "-":
        result = x - y
    elif requested_operation == "*":
        result = x * y
    elif requested_operation == "/":
        if y == 0: 
            print("Division by 0.")
            result = None
        else: 
            result = x / y

    return result

def calculator_main():
    invalid_input_warning = "Cannot calculate, invalid input. Try again."
    user_input = input("Calculate:").replace(" ", "")

    if user_input.lower() == "q":
        return "quit_flag"

    else: 
        result = calculate(*convert(user_input))

        if result != None:
            print("RESULT: %.2f\n----------" %(result))
        else: 
            print(invalid_input_warning)

        return result

def bye(): 
    bye_message = "BYE BYE!"
    display_message = ""

    for n in range(len(bye_message)+1): 
        display_message = bye_message[:n]
        print(display_message, end="\r")
        time.sleep(.1)
    print(display_message)

instruction() 

while True:
    output = calculator_main()

    if output == "quit_flag":
        break

bye()