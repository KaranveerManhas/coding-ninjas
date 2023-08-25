""" 
Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.
Note : For this question, you can assume that 0 raised to the power of 0 is 1


Input format :
Two integers x and n (separated by space)
Output Format :
x^n (i.e. x raise to the power n)
Constraints:
0 <= x <= 8 
0 <= n <= 9
Sample Input 1 :
 3 4
Sample Output 1 :
81
Sample Input 2 :
 2 5
Sample Output 2 :
32

"""

## Write your code here
## To take space separated input for two variables, we use the following syntax (3 lines)
## a, b = input().split()
## a = int(a)
## b = int(b)

def power_Of_Number(x,n):

    if n==0 :
        return 1
    if n==1:
        return x
    return x*power_Of_Number(x,n-1)






a,b=input().split()

a=int(a)
b=int(b)

p=power_Of_Number(a,b)
print(p)