""" 
A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. 
Implement a method to count how many possible ways the child can run up to the stairs. You need to return number of possible ways W.
Input format :
Integer N
Output Format :
Integer W
Constraints :
1 <= N <= 30
Sample Input 1 :
4
Sample Output 1 :
7
Sample Input 2 :
5
Sample Output 2 :
13

"""
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def staircase(n):

    if n<0:
        return 0
    if n==0:
        return 1
    
    n1= staircase(n-1)
    n2= staircase(n-2)
    n3= staircase(n-3)

    return n1 + n2 + n3


n=int(input())

print(staircase(n))