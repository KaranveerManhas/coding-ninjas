""" 
You have been given a singly linked list of integers along with two integers, 'i,' and 'j.' Swap the nodes that are present at the 'i-th' and 'j-th' positions.
Note :
Remember, the nodes themselves must be swapped and not the datas.

No need to print the list, it has already been taken care. Only return the new head to the list.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first line of each test case or query contains the elements of the singly linked list separated by a single space.

The second line of input contains two integer values 'i,' and 'j,' respectively. A single space will separate them.
 Remember/consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
Output format :
For each test case/query, print the elements of the updated singly linked list.

Output for every test case will be printed in a seperate line.
Constraints :
1 <= t <= 10^2
0 <= M <= 10^5
Where M is the size of the singly linked list.
0 <= i < M
0 <= j < M

Time Limit: 1sec
Sample Input 1 :
1
3 4 5 2 6 1 9 -1
3 4
Sample Output 1 :
3 4 5 6 2 1 9 
 Sample Input 2 :
2
10 20 30 40 -1
1 2
70 80 90 25 65 85 90 -1
0 6
 Sample Output 2 :
10 30 20 40 
90 80 90 25 65 85 70 

"""

def swapNodes(head, i, j) :

    if i > j:
        i, j = j, i
    
    if i == 0:
        if j == 1:
            cur = head.next
            head.next = cur.next
            cur.next = head
            return cur
        pt = head
        for c in range(1, j):
            pt = pt.next
        temp = head.next
        cur = pt.next
        head.next = cur.next
        pt.next = head
        cur.next = temp
        return cur
    if j - i == 1:
        pt = head
        for c in range(1, i):
            pt = pt.next
        cur = pt.next
        cur1 = cur.next
        cur.next = cur1.next
        pt.next = cur1
        cur1.next = cur
        return head
    pt1 = head
    pt2 = head
    for c in range(1, i):
        pt1 = pt1.next
    for c in range(1, j):
        pt2 = pt2.next
    cur1 = pt1.next
    cur2 = pt2.next
    temp = cur1.next
    cur1.next = cur2.next
    pt2.next = cur1
    pt1.next = cur2
    cur2.next = temp
    return head


