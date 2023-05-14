""" 
Print the following pattern for the given N number of rows.
Pattern for N = 4
    1
   12
  123
 1234
The dots represent spaces.


Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 50
Sample Input 1:
3
Sample Output 1:
      1 
    12
  123
Sample Input 2:
4
Sample Output 2:
      1 
    12
  123
1234


"""

## Read input as specified in the question
## Print the required output in given format
N=int(input())
i=1
while i<=N:
    sp=1
    while sp<=N-i:
        print(' ',end="")
        sp=sp+1
    st=1
    while st<=i:
        print(st,end="")
        st+=1
    print()
    i=i+1
