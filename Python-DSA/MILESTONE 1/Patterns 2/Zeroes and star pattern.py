""" 
Print the following pattern

Pattern for N = 4
*000*000*
0*00*00*0
00*0*0*00
000***000

Input Format :
N (Total no. of rows)

Output Format :
Pattern in N lines

Sample Input 1 :
3

Sample Output 1 :
*00*00*
0*0*0*0
00***00

Sample Input 2 :
5

Sample Output 2 :
*0000*0000*
0*000*000*0
00*00*00*00
000*0*0*000
0000***0000

"""

from os import *
from sys import *
from collections import *
from math import *

N=int(input())
i=N-1
k=0
while i>=0:
    print("0"*k+"*"+"0"*i+"*"+"0"*i+"*"+"0"*k,end="")
    print()
    k+=1
    i=i-1