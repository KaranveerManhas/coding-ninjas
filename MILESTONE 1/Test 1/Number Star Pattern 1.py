""" 
Print the following pattern for given number of rows.
Input format :
Integer N (Total number of rows)
Output Format :
Pattern in N lines
Sample Input :
   5
Sample Output :
 5432*
 543*1
 54*21
 5*321
 *4321

"""

from os import *
from sys import *
from collections import *
from math import *

n=int(input())

for i in range(1,n+1):
    #first half of pattern
    for j in range(n,i,-1):
        print(j,end="")
    #second half of pattern
    for j in range(n,n-1,-1):
        print("*",end="")
    #third half of pattern 
    for j in range(i,1,-1):
        print(j-1,end="")
    print()