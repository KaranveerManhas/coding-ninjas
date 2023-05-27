""" 
Provided with a random integer array/list(ARR) of size N, you have been required to sort this array using 'Selection Sort'.
 Note:
Change in the input array/list itself. You don't need to return or print the elements.
Input format :
First line contains an integer 'N' representing the size of the array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.
Output format :
For each test case, print the elements of the array/list in sorted order separated by a single space.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^3
Time Limit: 1 sec
Sample Input 1:
7
2 13 4 1 3 6 28
Sample Output 1:
1 2 3 4 6 13 28
Sample Input 2:
5
9 3 6 2 0
Sample Output 2:
0 2 3 6 9

"""
from sys import stdin

def selectionSort(arr, n) :
    #Your code goes here
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    
    return






