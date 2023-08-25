""" 
Check whether a given String S is a palindrome using recursion. Return true or false.
Input Format :
String S
Output Format :
'true' or 'false'
Constraints :
0 <= |S| <= 1000
where |S| represents length of string S.
Sample Input 1 :
racecar
Sample Output 1:
true
Sample Input 2 :
ninja
Sample Output 2:
false

"""
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def palindrome(s,st,en):

    if st>en:
        return True
    
    if s[st]!=s[en]:
        return False
    
    return palindrome(s,st+1,en-1)






s=input()

a= palindrome(s, 0,len(s)-1)

if a:
    print("true")
else:
    print("false")