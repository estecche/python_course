"""
Does it have all vowels?

Write a program that inputs two strings and finds out whether it(each) has all the vowels.
Vowels are basic alphabets in English which make vowel sounds .(a,e,i,o,u)

If the input string has all the vowels then print "YES" otherwise print "NO".
There are many ways to solve this problem, make sure to really think about the solution and do it yourself
by restricting yourself to only use loops, dictionaries, lists (the things we have studied before).

Example Input #1:

This house is pretty

There is a candy shop near the bridge for university students

Example Output #1:
NO
YES

In the first sentence we dont have all the vowels {a,e,i,o,u} in the second one we have.

Hint/remember:
You can iterate over strings like lists.
"""
text1 = input()
text2 = input()
vowels = {
    "a" : 0,
    "e" : 0,
    "i" : 0,
    "o" : 0,
    "u" : 0
}
results = {
    1 : 0,
    2 : 0
}
i = 1
for text in [text1,text2]:
    for key in vowels.keys():
        vowels[key] = 0

    for character in range(0, len(text)):
        if text[character] == 'a':
            vowels["a"] = 1
        elif text[character] == 'e':
            vowels["e"] = 1
        elif text[character] == 'i':
            vowels["i"] = 1
        elif text[character] == 'o':
            vowels["o"] = 1
        elif text[character] == 'u':
            vowels["u"] = 1
    
    results[i] = vowels["a"] + vowels["e"] + vowels["i"] + vowels["o"] + vowels["u"]
    i += 1

for key in results.keys():
    if results[key] == 5:
        print("YES")
    else :
        print("NO")