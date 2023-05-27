""" 
Print the following pattern for the given number of rows.
Note: N is always odd.


Pattern for N = 5



The dots represent spaces.



Input format :
N (Total no. of rows and can only be odd)
Output format :
Pattern in N lines
Constraints :
1 <= N <= 49
Sample Input 1:
5
Sample Output 1:
  *
 ***
*****
 ***
  *
Sample Input 2:
3
Sample Output 2:
  *
 ***
  *

"""

from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
N=int(input())
for i in range(1, N+1):
    i = i - (N//2 +1)
    if i < 0:
        i = -i
    print(" " * i + "*" * (N - i*2) + " "*i)