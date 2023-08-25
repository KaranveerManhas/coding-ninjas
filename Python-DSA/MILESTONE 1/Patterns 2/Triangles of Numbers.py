"""" 
Print the following pattern for the given number of rows.
Pattern for N = 4
           1
          232
         34543
        4567654

The dots represent spaces.

Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines

Constraints :
0 <= N <= 50

Sample Input 1:
5

Sample Output 1:
           1
         232
       34543
     4567654
   567898765
   
Sample Input 2:
4

Sample Output 2:
           1
          232
         34543
        4567654

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
        print(i+j-1,end="")
        j+=1
    #decreasing sequence
    p=i
    while p>=2:
        print(i-2+p,end="")
        p= p-1
    print()
    i=i+1
    