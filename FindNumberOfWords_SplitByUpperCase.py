"""
 Given string “findThePerfectMatch”:
- Find how many words is there
- Convert the string to a correct sentence
"""

s = "findThePerfectMatch"
if s[0].isupper():
    count = 1
    for i in range(0, len(s)):
        if s[i].isupper():
            count += 1
        else:
            count = 1

s2 = s[0].capitalize()
for i in range(1, len(s)):
    if s[i].islower():
        s2 += s[i]
    else:
        s2 += ' '
        s2 += s[i].lower()

print("Correct sentence : " + str(s2))

# Define the number of words in spited string
res = len(s2.split())

# printing result
print("The number of words in string are : " + str(res))

