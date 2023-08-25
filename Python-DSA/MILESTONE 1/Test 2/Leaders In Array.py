"""  
Given an integer array A of size n. Find and print all the leaders present in the input array. An array element A[i] is called Leader, 
if all the elements following it (i.e. present at its right) are less than or equal to A[i].
Print all the leader elements separated by space and in the same order they are present in the input array.
Input Format :
Line 1 : Integer n, size of array
Line 2 : Array A elements (separated by space)
Output Format :
 leaders of array (separated by space)
Constraints :
1 <= n <= 10^6
Sample Input 1 :
6
3 12 34 2 0 -1
Sample Output 1 :
34 2 0 -1
Sample Input 2 :
5
13 17 5 4 6
Sample Output 2 :
17 6

"""

## Read input as specified in the question.
## Print output as specified in the question.

n= int(input())

A= [int(x) for x in input().split()][:n]

for i in range(n-1):
    
    for j in range(i+1,n):
        if A[i]<A[j]:
            break
    else:
        print(A[i],end=" ")
print(A[n-1])