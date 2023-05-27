""" 
Print the following pattern for the given number of rows.
Pattern for N = 4
4444444
4333334
4322234
4321234
4322234
4333334  
4444444
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
3
Sample Output :
33333
32223
32123
32223
33333

"""


from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())

#Printing Upper half of Inner Reducing Pattern
for i in range(n,0,-1):
    #first part of upper half
    for j in range(n,i,-1):
        print(j,end="")
    #second part of upper half
    for j in range(1,i*2-1):
        print(i,end="")
    #third part of upper half
    for j in range(i,n+1):
        print(j,end="")
    print()
#Printing Lower Half of Inner Reducing Pattern
for i in range(1,n):
    #first part of lower half
    for j in range(n,i,-1):
        print(j,end="")
    #second part of lower half
    for j in range(1,i*2,1):
        print(i+1,end="")
    #third part of lower half
    for j in range(i+1,n+1):
        print(j,end="")
    print()