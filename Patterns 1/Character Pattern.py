""" 
Print the following pattern for the given N number of rows.
Pattern for N = 4
A
BC
CDE
DEFG

Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines

Constraints
0 <= N <= 13

Sample Input 1:
5

Sample Output 1:
A
BC
CDE
DEFG
EFGHI

Sample Input 2:
6

Sample Output 2:
A
BC
CDE
DEFG
EFGHI
FGHIJK

"""

## Read input as specified in the question
## Print the required output in given format
N=int(input())

i=65
lim=i+N-1

while i<=lim:
    j=65
    start=i+1-1
    while j<=i:
        print(chr(start), end="")
        j=j+1
        start+=1
    print()
    i=i+1
        