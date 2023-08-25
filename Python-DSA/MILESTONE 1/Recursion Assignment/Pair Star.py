""" 
Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
Input format :
String S
Output format :
Modified string
Constraints :
0 <= |S| <= 1000
where |S| represents length of string S.
Sample Input 1 :
hello
Sample Output 1:
hel*lo
Sample Input 2 :
aaaa
Sample Output 2 :
a*a*a*a

"""
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def pairstar(string,string2,i=0):
    
    string2+=string[i]

    if i==len(string)-1:
        print(string2)
        return

    if string[i]==string[i+1]:
        string2+="*"
        
    
    pairstar(string,string2,i+1)

string = input()
string2=""
pairstar(string,string2)