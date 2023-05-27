""" 
Sort an array A using Quick Sort.
Change in the input array itself. So no need to return or print anything.


Input format :
Line 1 : Integer n i.e. Array size
Line 2 : Array elements (separated by space)
Output format :
Array elements in increasing order (separated by space)
Constraints :
1 <= n <= 10^3
Sample Input 1 :
6 
2 6 8 5 4 3
Sample Output 1 :
2 3 4 5 6 8
Sample Input 2 :
5
1 2 3 5 7
Sample Output 2 :
1 2 3 5 7 

"""
def partition(arr,start,end):
    pivot= arr[end]
    i=start-1
    
    for j in range(start,end):
        if arr[j]<=pivot:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    
    arr[i+1],arr[end]=arr[end],arr[i+1]
    
    return i+1


def quickSort(arr, start, end):
    # Please add your code here
    if start<end:
        part= partition(arr,start,end)
        
        quickSort(arr,start,part-1)
        
        quickSort(arr,part+1,end)


n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n-1)
print(*arr)
