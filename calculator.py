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
# [] making calculations
#       [] write calculation functions
#       [] call the right funtion
# [] displaying result
# [] add testing 
# [] finalise intro text

# Input criteria
# -> one line / one input
# -> start with 2 numbers 
# -> 1 operation

welcome_message = "Welcome to the calculator. \n----------\nThe below operations are possible: \naddition \t-> + \nsubtraction \t-> - \nmultiplication \t-> * \ndivision \t-> / \n----------"

print(welcome_message)

user_input = input("Calculate:")

user_input = user_input.replace(" ", "")

print(user_input)

# possible_operations = {
#     "addition": {
#         "use": False,
#         "marker": "+",
#         "operation": +, 
#         }

# }

# addition = user_input.find("+")
# substraction = user_input.find("-")
# multiplication = user_input.find("*")
# division = user_input.find("/")

possible_operations = ["+", "-", "*", "/"]

requested_operation = ""

#need my numbers defined by this point
#need to save input find

x = 0
y = 0

for el in possible_operations: 
    operator_index = user_input.find(el)
    if operator_index > -1: 
        x = eval(user_input[0:operator_index])
        y = eval(user_input[operator_index+1:])
        requested_operation = el
        break

print("%.2f -> first number \n%.2f -> second number \n%s operation to perform" %(x, y, requested_operation))


# if user_input.find("+") > -1: 
#     requested_operation = "addition"
#     #use an addition funtion
# elif user_input.find("-") > -1: 
#     # use a substraction funtion
# elif user_input.find("*") > -1: 
#     # use a multiplication funtion
# elif user_input.find("/") > -1: 
#     # use a division funtion

# substraction = 
# multiplication = user_input.find("*")
# division = user_input.find("/")





#  |  find(...)
#  |      S.find(sub[, start[, end]]) -> int
#  |      
#  |      Return the lowest index in S where substring sub is found,
#  |      such that sub is contained within S[start:end].  Optional
#  |      arguments start and end are interpreted as in slice notation.
#  |      
#  |      Return -1 on failure.

#   |  index(...)
#  |      S.index(sub[, start[, end]]) -> int
#  |      
#  |      Return the lowest index in S where substring sub is found,
#  |      such that sub is contained within S[start:end].  Optional
#  |      arguments start and end are interpreted as in slice notation.
#  |      
#  |      Raises ValueError when the substring is not found.

#   |  split(self, /, sep=None, maxsplit=-1)
#  |      Return a list of the words in the string, using sep as the delimiter string.
#  |      
#  |      sep
#  |        The delimiter according which to split the string.
#  |        None (the default value) means split according to any whitespace,
#  |        and discard empty strings from the result.
#  |      maxsplit
#  |        Maximum number of splits to do.
#  |        -1 (the default value) means no limit.


