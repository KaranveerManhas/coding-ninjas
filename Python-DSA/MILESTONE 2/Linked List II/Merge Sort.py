""" 
 Given a singly linked list of integers, sort it using 'Merge Sort.'
Note :
No need to print the list, it has already been taken care. Only return the new head to the list.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first and the only line of each test case or query contains the elements of the singly linked list separated by a single space.
Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
Output format :
For each test case/query, print the elements of the sorted singly linked list.

Output for every test case will be printed in a seperate line.
Constraints :
1 <= t <= 10^2
0 <= M <= 10^5
Where M is the size of the singly linked list.

Time Limit: 1sec
Sample Input 1 :
1
10 9 8 7 6 5 4 3 -1
Sample Output 1 :
 3 4 5 6 7 8 9 10 
 Sample Input 2 :
2
-1
10 -5 9 90 5 67 1 89 -1
Sample Output 2 :
-5 1 5 9 10 67 89 90 

"""

def findMid(head):
    if head is None:
        return head
    
    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow =slow.next
        fast = fast.next.next
    
    return slow

def merge(h1, h2):

    if h1 is None or h2 is None:
        return h1 or h2
    
    if h1.data<=h2.data:
        finalhead =h1
        finaltail = h1
        h1 = h1.next
    else:
        finalhead = h2
        finaltail = h2
        h2 = h2.next 
    
    while h1 is not None and h2 is not None:
        if h1.data<=h2.data:
            finaltail.next = h1
            finaltail = h1
            h1 = h1.next
        
        else:
            finaltail.next = h2
            finaltail = h2
            h2 = h2.next
    
    if h1 is not None:
        while h1 is not None:
            finaltail.next = h1
            finaltail = h1
            h1 = h1.next
        
    if h2 is not None:
        while h2 is not None:
            finaltail.next = h2
            finaltail = h2
            h2 = h2.next
    
    return finalhead

def mergeSort(head) :
	#Your code goes here
    if head is None or head.next is None:
        return head
    
    mid = findMid(head)
    head2 = mid.next
    mid.next = None

    h1 = mergeSort(head)
    h2 = mergeSort(head2)

    finalHead = merge(h1,h2)

    return finalHead


