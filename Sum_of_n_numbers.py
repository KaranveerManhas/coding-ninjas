""" 
Given an integer n, find and print the sum of numbers from 1 to n.

Note :

Use while loop only.

Input Format :
Integer n

Output Format :
Sum of numbers

Constraints :
1 <= n <= 100

Sample Input :
10

Sample Output :
55 
    
"""

n = int(input())
i=0
while n>0:
    i=i+n
    n=n-1

print(i)
