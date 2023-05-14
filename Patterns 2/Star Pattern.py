""" 
Print the following pattern
Pattern for N = 4
    *
   *** 
  *****
 *******

The dots represent spaces.

Input Format :
N (Total no. of rows)

Output Format :
Pattern in N lines

Constraints :
0 <= N <= 50

Sample Input 1 :
3

Sample Output 1 :
   *
  *** 
 *****
 
Sample Input 2 :
4

Sample Output 2 :
    *
   *** 
  *****
 *******

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
        print("*",end="")
        j+=1
    #decreasing sequence
    p=i-1
    while p>=1:
        print("*",end="")
        p= p-1
    print()
    i=i+1
    