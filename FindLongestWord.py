"""
 Given sentence, for example: “Learn the basics of the most popular programming language"
 - find the longest word
 - find number of words in sentence

"""

test_string = "Learn the basics of the most popular programming language"

# Printing original string
print("The original string is : " + test_string)

# Finding the longest word
wordsList = test_string.split()
maxWord = wordsList[0]
print(wordsList)
for w in wordsList[1:]:
    if len(w) > len(maxWord):
        maxWord = w

print("Longest word:", maxWord)
print("Length:", len(maxWord))

# Using split()to count words in string
res = len(test_string.split())

# Printing result
print("The number of words in string are : " + str(res))

# Task #2
# Print all words in column + number of symbols
# def find_longest_word(word_list):
#     for word in word_list:
#             print(word, len(word))
#
#
# words = input('Please enter your sentence')
# word_list = words.split()
# find_longest_word(word_list)
