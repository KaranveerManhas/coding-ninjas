""" 
Given an integer array A of size N, check if the input array can be splitted in two parts such that -
- Sum of both parts is equal
- All elements in the input, which are divisible by 5 should be in same group.
- All elements in the input, which are divisible by 3 (but not divisible by 5) should be in other group.
- Elements which are neither divisible by 5 nor by 3, can be put in any group.
Groups can be made with any set of elements, i.e. elements need not to be continuous. And you need to consider each and every element of input array in some group.
Return true, if array can be split according to the above rules, else return false.
Note : You will get marks only if all the test cases are passed.
Input Format :
Line 1 : Integer N (size of array)
Line 2 : Array A elements (separated by space)
Output Format :
true or false
Constraints :
1 <= N <= 50
Sample Input 1 :
2
1 2
Sample Output 1 :
false
Sample Input 2 :
3
1 4 3
Sample Output 2 :
true

"""



def split(arr,n,i,lsum,rsum):
    #Implement Your Function here
    if i==n:
        return lsum == rsum
    
    if arr[i]%5==0:
        lsum+=arr[i]
    
    elif arr[i]%3==0:
        rsum+=arr[i]
    
    else:
        return split(arr,n,i+1,lsum + arr[i], rsum) or split(arr,n,i+1,lsum, rsum + arr[i])
    
    return split(arr, n, i+1, lsum, rsum)
    
n = int(input())
arr = [int(ele) for ele in input().split()]
ans = split(arr,n,0,0,0)
if ans is True:
    print('true')
else:
    print('false')