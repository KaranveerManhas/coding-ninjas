""" 
Print the following pattern for a given n.
For eg. N = 6
123456
  23456
    3456
      456
        56
          6
        56
      456
    3456
  23456
123456

Sample Input 1 :
4

Sample Output 1 :
1234
  234
    34
      4
    34
  234
1234

"""
from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
N=int(input())

for i in range(1,N,1):
    #upper half spaces
    for s in range(1,i,1):
        print(" ", end="")
    #upper half sequence
    for j in range(i,N+1,1):
        print(j,end="")
    print()
for i in range(N,0,-1):
    #lower half spaces
    for s in range(i-1):
        print(" ", end="")
    #lower half sequence
    for k in range(i,N+1,1):
        print(k,end="")
    print()