"""
This is an example about dictionaries.
"""
book = {
    "title" : "From the Earth to the Moon",
    "author" : {
        "first_name": "Jules",
        "last_name": "Verne"
    },
    "pages" : 240
}
author_name = book["author"]
print(author_name["first_name"] + " " + author_name["last_name"])

# we can also add something new into the dictionary
book["year"] = 2020
print("Year of the book: ", book["year"])

# .. and modify it
book["year"] = 2021
print("Year of the book: ", book["year"])

print("Book: ", book)

# getting all the keys
print("Keys: ", book.keys())

person_one = {
    "name" : "Person 1",
    "last_name" : "Last Name 1",
    "age" : 20
}

person_two = {
    "name" : "Person 2",
    "last_name" : "Last Name 2",
    "age" : 25
}

persons = [person_one, person_two]
print("Persons: ", persons)
print("Person 1: ", persons[0])

university = {
    "students" : [
        person_one, person_two
    ]
}
print(university)
print("Student 1: ", university["students"][0])