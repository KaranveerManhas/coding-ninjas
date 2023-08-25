""" 
Print the following pattern for the given number of rows.
Pattern for N = 4
1111
000
11
0
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
5
Sample Output :
11111
0000
111
00
1

"""

from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
a=int(input())

for i in range(a,0,-2):
    print("1"*i+"\n",end="")
    print("0"*(i-1)+"\n",end="")
print()
