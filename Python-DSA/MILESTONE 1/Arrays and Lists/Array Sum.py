""" 
Given an array of length N, you need to find and print the sum of all elements of the array.
Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Output Format :
Sum
Constraints :
1 <= N <= 10^6
Note:
It is advisable to declare an array with a size that can accommodate all the elements, considering that N has a maximum value of 10^5.
Sample Input :
3
9 8 9
Sample Output :
26

"""
# Read input as sepcified in the question
# Print output as specified in the question
n=int(input())

li = [int(x) for x in input().split()]
sum=0
for i in range(len(li)):
    sum=sum+li[i]
print(sum)