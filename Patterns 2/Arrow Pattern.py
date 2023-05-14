""" 
Print the following pattern for the given number of rows.
Assume N is always odd.

Note : There is space after every star.

Pattern for N = 7
*
 * *
   * * *
     * * * *
   * * *
 * *
*

Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines

Sample Input :
11

Sample Output :
*
 * *
   * * *
     * * * *
       * * * * *
         * * * * * *
       * * * * *
     * * * *
   * * *
 * *
*

"""

## Read input as specified in the question.
## Print output as specified in the question.
N=int(input())
i=1
rem=N//2
while i<=rem:
    #spaces
    sp=2
    while sp<=i:
        print(" ",end="")
        sp=sp+1
    #first half of arrow 
    j=1
    while j<=i:
        print("* ",end="")
        j+=1
    print()
    i=i+1
i=rem+1
while i>=1:
    #spaces
    sp=i-2
    while sp>=0:
        print(" ",end="")
        sp=sp-1
    #second half of arrow
    j=i
    while j>=1:
        print("* ",end="")
        j=j-1
    print()
    i=i-1
        
    