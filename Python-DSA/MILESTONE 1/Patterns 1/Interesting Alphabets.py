""" 
Print the following pattern for the given number of rows.
Pattern for N = 5
E
DE
CDE
BCDE
ABCDE

Input format :
N (Total no. of rows)

Output format :
Pattern in N lines

Constraints
0 <= N <= 26

Sample Input 1:
8

Sample Output 1:
H
GH
FGH
EFGH
DEFGH
CDEFGH
BCDEFGH
ABCDEFGH

Sample Input 2:
7

Sample Output 2:
G
FG
EFG
DEFG
CDEFG
BCDEFG
ABCDEFG

"""

from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
N=int(input())

i=65+N-1
lim =65
while i>=lim:
    j=i
    while j<=65+N-1:
        print(chr(j), end="")
        j=j+1
    print()
    i=i-1
