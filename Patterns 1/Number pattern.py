""" 
Print the following pattern for the given N number of rows.

Pattern for N = 4
1234
123
12
1

Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines

Sample Input :
5

Sample Output :
12345
1234
123
12
1

"""

from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
N=int(input())
i=N
while i>=1:
    j=i
    k=1
    while j>=1:
        print(k,end="")
        k=k+1
        j=j-1
        
    print()
    i=i-1
