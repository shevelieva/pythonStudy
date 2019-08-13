# Check a Given Word or String is Palindrome or Not
# String example: Never odd or even


def is_palindrome(value):
    min = 0
    max = len(value) - 1

    # Scan string for letter equality at each end.
    # Move indexes closer to the center after each check.
    while True:

        # Return true if all characters were checked.
        if min > max:
            return True;

        a = value[min]
        b = value[max]

        # Return false is characters are not equal.
        if a != b:
            return False;

        # Move inwards.
        min += 1
        max -= 1

lines = ["civic",
    "A man, a plan, a canal: Panama.",
    "Cigar? Toss it in a can. It is so tragic.",
    "This article is not useful."]

# Use to translate punctuation to spaces.
# ... Changes uppercase to lowercase.
dict = str.maketrans(",:.'!?ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "      abcdefghijklmnopqrstuvwxyz")

for line in lines:
    # Change all punctuation to spaces.
    line = line.translate(dict)

    # Remove all spaces.
    line = line.replace(" ", "")

    # See if line is a palindrome.
    if is_palindrome(line):
        print("Palindrome:    ", line)
    else:
        print("Not palindrome:", line)


## Task #2 create function which return reverse of a string
#             def reverse(s):
#                 return s[::-1]
#
#
#             def isPalindrome(s):
#                 # Calling reverse function
#                 rev = reverse(s)
#
#                 # Checking if both string are equal or not
#                 if (s == rev):
#                     return True
#                 return False
#
#
#             # Driver code
#             s = "malayalam"
#             ans = isPalindrome(s)
#
#             if ans == 1:
#                 print("Yes")
#             else:
#                 print("No")

# # This check works just for single word
# string = input("Please enter your own String : ")
#
# if string == string[:: - 1]:
#     print("This is a Palindrome String")
# else:
#     print("This is Not a Palindrome String")
#
# string = input("Please enter your own String : ")
# flag = 0
#
# length = len(string)
# for i in range(length):
#     if string[i] != string[length - i - 1]:
#         flag = 1
#         break
#
# if flag == 0:
#    print("This is a Palindrome String")
# else:
#    print("This is Not a Palindrome String")