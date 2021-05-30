"""
These are examples about booleans and conditionals
"""
is_valid = True
if is_valid:
    print("It is valid!")
# The following means also true
if 1:
    print("It is 1!")
# The following means false
if None:
    print("It is valid!")
    print("This won't get printed at all")
# The following means true
if "False":
    print("It is True!")
# if / else statement
if not is_valid:
    print("It is valid!")
else :
    print ("It is not valid!")
# if / else chain
if not is_valid:
    print("It is valid chain!")
elif is_valid:
    print("It is valid chain!")
    print("also printing this inside the if")
