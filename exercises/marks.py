"""
In this exercise you will have to write code that inputs marks between 0 and 100 of 5 different subjects.
You have to print the grades (Letters) given the following criteria in the range of marks(inclusive).

Marks : Grade
90-100: A
80-89: B
70-79: C
60-69: D
50-59: E
0-49: F

Example Input:
56
67
34
76
98

Example Output:
EDFCA

"""
marks = []
#taking in the input for 5 marks from the user and adding it to the list
for i in range(5):
    marks.append(int(input()))
# now that we have all the marks we can just loop over it
output = ""
for mark in marks:
    if mark >= 90 and mark <= 100:
        output += "A"
        continue
    if mark >= 80 and mark < 90:
        output += "B"
        continue
    if mark >= 70 and mark < 80:
        output += "C"
        continue
    if mark >= 60 and mark < 70:
        output += "D"
        continue
    if mark >= 50 and mark < 60:
        output += "E"
        continue
    else :
        output += "F"

#now we simply print the output
print(output)