""" 
You are given an array of integers that contain numbers in random order. Write a program to find and return the number which occurs the maximum times in the given input.
If two or more elements are having the maximum frequency, return the element which occurs in the array first.
Input Format:
The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol N.
The following line contains N space separated integers, that denote the value of the elements of the array.
Output Format :
The first and only line of output contains most frequent element in the given array.
Constraints:
0 <= N <= 10^8
Time Limit: 1 sec
Sample Input 1 :
13
2 12 2 11 12 2 1 2 2 11 12 2 6 
Sample Output 1 :
2
Sample Input 2 :
3
1 4 5
Sample Output 2 :
1

"""

    # Read input as sepcified in the question
# Print output as specified in the question

import math as mt

def mostFrequent(arr, n):

	dict = {}

	for num in arr:
		if num in dict:
			dict[num] += 1
		else:
			dict[num] = 1
	
	ans = arr[0]

	for nums in arr:
		if dict[nums] > dict[ans]:
			ans = nums
	
	return ans

n = int(input())

arr = list(map(int, input().split()))

print(mostFrequent(arr, n))


