# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
# # Complete the marsExploration function below.
# def marsExploration(S):
#
#     S=raw_input()
# assert len(S)%3==0 and len(S)<=99
# n=len(S)/3
# exp="SOS"*n #Expected string
# ans=0
# for i in range(len(S)):
#     if exp[i]!=S[i]:
#         ans=ans+1
# print ans
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = input()
#
#     result = marsExploration(s)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
