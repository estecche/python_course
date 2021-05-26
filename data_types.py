"""
This is an example of several data types in Python
"""
# string
name = "my name"
single_quotes_name = 'single quotes'
print("The length of name is: ", len(name))
print("In upper case : " + name.upper())
print("In lower case: " + name.lower())

# About single and double quotes. We can use double quotes if our string contains single quotes
double_quotes = "Hi, it's raining!"
print(double_quotes)

triple_quotes = '''This is an "example" of mixing things, since it's a mixed string.'''
print(triple_quotes)
print("-----------------------")
# number
number = 12.0
x = 37;
y = 23;
float_division = x / y
print("Float division = ", float_division)
floor_division = x // y
print("Floor division = ", floor_division)
mod_division = x % y
print("Module of the division = ", mod_division)

# This is equal to 4^2
exponential = 4 ** 2
print("Two times 4 is = ", exponential)

print("-----------------------")
# list
numbers = [10, 20, 15]
print("all numbers = ", numbers)
print("first position of the list = ", numbers[0])

# dictionary
book = {
    "title" : "this is the title",
    "pages" : 30,
    "price" : 145.5
}
print(book["price"])