""" 
Print the following pattern for the given N number of rows.

Pattern for N = 3
 A
 BB
 CCC
 
Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines

Constraints
0 <= N <= 26

Sample Input 1:
7

Sample Output 1:
A
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGG

Sample Input 2:
6

Sample Output 2:
A
BB
CCC
DDDD
EEEEE
FFFFFF

"""

from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
k=int(input())

i=65
lim=i+k-1

while i<=lim:
    j=65
    while j<=i:
        print(chr(i), end="")
        j=j+1
    print()
    i=i+1
        