""" 
Print the following pattern for the given N number of rows.

Pattern for N = 4
1
11
111
1111

Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines

Sample Input :
5

Sample Output :
1
11
111
1111
11111

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
    j=1
    while j<=i:
        print(1,end="")
        j=j+1
        
    print()
    i+=1
