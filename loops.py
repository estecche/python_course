"""
These are examples of loops
"""
my_list = [10, 4, 5, 8]
# while loop
i = 0
while i < len(my_list):
    if i == 1:
        i += 1
        continue
    if i == 2:
        break
    print("The value is = " + str(my_list[i]))
    i += 1
print("------------")
for j in range(len(my_list)):
    print("The value is = " + str(my_list[j]))
# You can tell the range function where to start
print("------------")
for j in range(2, len(my_list)):
    print("The value is = " + str(my_list[j]))
# You can also tell the range function the increment
print("------------")
for j in range(0, len(my_list), 2):
    print("(step) The value is = " + str(my_list[j]))
print("------------")
for n in my_list:
    print("(n) The value is = " + str(n))

book = {
    "title" : "From the Earth to the Moon",
    "author" : "Jules Verne",
    "pages" : 240
}
print("------------")
for key in book:
    print("(book) " + key + " = " + str(book[key]))