""" 

Given an array consisting of positive and negative integers, find the length of the longest subarray whose sum is zero.
Input Format:
The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol N.
The following line contains N space separated integers, that denote the value of the elements of the array.
Output Format
The first and only line of output contains length of the longest subarray whose sum is zero.
Constraints:
0 <= N <= 10^8
Time Limit: 1 sec
Sample Input 1:
10 
 95 -97 -387 -435 -5 -70 897 127 23 284
Sample Output 1:
5
Explanation:
The five elements that form the longest subarray that sum up to zero are: -387, -435, -5, -70, 897 
Note
You don't have to print anything. Just complete the definition of the function given and return the value accordingly.

"""

def subsetSum(l):
    cumulativeSum ={}
    longestSubarray =0
    sumx = 0
    for i in range(len(l)):
        sumx += l[i]
        if sumx == 0:
            longestSubarray = i+1
        elif sumx in cumulativeSum:
            longestSubarray = max(longestSubarray, i-cumulativeSum[sumx])
        else:
            cumulativeSum[sumx] = i
    
    return longestSubarray
     


# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(subsetSum(l))