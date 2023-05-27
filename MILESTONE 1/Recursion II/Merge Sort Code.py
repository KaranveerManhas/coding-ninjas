"""  
Given the starting 'l' and the ending 'r' positions of the array 'ARR', your task is sorting the elements between 'l' and 'r'.
Note:
Change in the input array itself. So no need to return or print anything.
Example:
Input: ‘N’ = 7,
'ARR' = [2, 13, 4, 1, 3, 6, 28]

Output: [1 2 3 4 6 13 28]

Explanation: After applying 'merge sort' on the input array, the output is [1 2 3 4 6 13 28].
Input format :
The first line contains an integer 'N' representing the size of the array/list.

The second line contains 'N' single space-separated integers representing the elements in the array/list.
Output format :
You don't need to return anything. In the output, you will see the array after modification is done by you.
Constraints :
1 <= N <= 10^3
0 <= ARR[i] <= 10^9
Sample Input 1:
7
2 13 4 1 3 6 28
Sample Output 1:
1 2 3 4 6 13 28
Explanation of Sample Output 1:
After applying 'merge sort' on the input array, the output is [1 2 3 4 6 13 28].
Sample Input 2:
5
9 3 6 2 0
Sample Output 2:
0 2 3 6 9
Explanation of Sample Output 2:
After applying 'merge sort' on the input array, the output is [0 2 3 6 9].

"""
def merge(arr1,arr2,arr):
    i=0
    j=0
    k=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr[k]=arr1[i]
            i+=1
            k+=1
        else:
            arr[k]=arr2[j]
            j+=1
            k+=1
    
    while i<len(arr1):
        arr[k]=arr1[i]
        i+=1
        k+=1
    while j<len(arr2):
        arr[k]=arr2[j]
        j+=1
        k+=1



def mergeSort(arr):
    # Please add your code here
    if len(arr)==0 or len(arr)==1:
        return
    
    mid= len(arr)//2
    arr1=arr[0:mid]
    arr2=arr[mid:]
    
    mergeSort(arr1)
    
    mergeSort(arr2)

    merge(arr1,arr2,arr)
    

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr)
print(*arr)
