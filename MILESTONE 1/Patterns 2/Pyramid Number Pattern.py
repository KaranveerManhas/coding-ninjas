""" 
Print the following pattern for the given number of rows.
Pattern for N = 4
   1
  212
 32123
4321234

Input format : 
N (Total no. of rows)

Output format : 
Pattern in N lines

Sample Input :
5

Sample Output :
        1
      212
    32123
  4321234
543212345

"""


from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
N=int(input())
i=1
while i<=N:
    #spaces
    sp=1
    while sp<=N-i:
        print(' ',end="")
        sp=sp+1
    #increasing sequence
    j=1
    while j<=i:
        print(i-j+1,end="")
        j+=1
    #decreasing sequence
    p=i-1
    while p>=1:
        print(i-p+1,end="")
        p= p-1
    print()
    i=i+1
    