""" 
Suppose you have a string, S, made up of only 'a's and 'b's. Write a recursive function that checks if the string was generated using the following rules:
a. The string begins with an 'a'
b. Each 'a' is followed by nothing or an 'a' or "bb"
c. Each "bb" is followed by nothing or an 'a'
If all the rules are followed by the given string, return true otherwise return false.
Input format :
String S
Output format :
'true' or 'false'
Constraints :
1 <= |S| <= 1000
where |S| represents length of string S.
Sample Input 1 :
abb
Sample Output 1 :
true
Sample Input 2 :
abababa
Sample Output 2 :
false
Explanation for Sample Input 2
In the above example, a is not followed by either "a" or "bb", instead it's followed by "b" which results in false to be returned.

"""

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def checkAB(string):

    if len(string)==0:
            return False

    if string[0]=='a':
        if len(string)==1:
            return True
        if string[1]=='a':
            return checkAB(string[1:])
        elif string[1]=='b' and string[2]=='b':
            return checkAB(string[1:])
        else:
            return False
    elif string[0]=='b' and string[1]=='b':
        if len(string)==2:
            return True
        elif string[2]=='a':
            return checkAB(string[2:])
        else:
            return False
    checkAB(string[1:])

string= input()

flag= (string[0] == 'a') and checkAB(string)
if flag:
    print("true")
else:
    print("false")