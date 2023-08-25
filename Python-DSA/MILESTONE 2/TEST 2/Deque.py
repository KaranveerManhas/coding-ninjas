""" 
You need to implement a class for Dequeue i.e. for double ended queue. In this queue, elements can be inserted and deleted from both the ends.
You don't need to double the capacity.
You need to implement the following functions -
1. constructor
You need to create the appropriate constructor. Size for the queue passed is 10.
2. insertFront -
This function takes an element as input and insert the element at the front of queue. Insert the element only if queue is not full. And if queue is full, print -1 and return.
3. insertRear -
This function takes an element as input and insert the element at the end of queue. Insert the element only if queue is not full. And if queue is full, print -1 and return.
4. deleteFront -
This function removes an element from the front of queue. Print -1 if queue is empty.
5. deleteRear -
This function removes an element from the end of queue. Print -1 if queue is empty.
6. getFront -
Returns the element which is at front of the queue. Return -1 if queue is empty.
7. getRear -
Returns the element which is at end of the queue. Return -1 if queue is empty.
Input Format:
For C++ and Java, input is already managed for you. You just have to implement given functions.

For Python:
The choice codes and corresponding input for each choice are given in a new line. The input is terminated by integer -1. 
The following table elaborately describes the function, their choice codes and their corresponding input - 
Alt Text

Output Format:
For C++ and Java, output is already managed for you. You just have to implement given functions.

For Python: 
The output format for each function has been mentioned in the problem description itself. 
Sample Input 1:
5 1 49 1 64 2 99 5 6 -1
Sample Output 1:
-1
64
99
Explanation:
The first choice code corresponds to getFront. Since the queue is empty, hence the output is -1. 
The following input adds 49 at the top and the resultant queue becomes: 49.
The following input adds 64 at the top and the resultant queue becomes: 64 -> 49
The following input add 99 at the end and the resultant queue becomes: 64 -> 49 -> 99
The following input corresponds to getFront. Hence the output is 64.
The following input corresponds to getRear. Hence the output is 99.

"""


from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
class Node():

    def __init__(self, data):
        self.data = data
        self.next = None


class Deque:
    def __init__(self):
        self.front=None
        self.dequeSize=0
   
    def insertFront(self,data):
        temp=Node(data)
        if self.front==None:
            self.front=temp
            self.dequeSize=self.dequeSize+1
        else:
            temp.next=self.front
            self.front=temp
            self.dequeSize=self.dequeSize+1

    def insertRear(self,data):
        temp=Node(data)
        if self.front==None:
            self.front=temp
            self.dequeSize=self.dequeSize+1
        else:
            curr=self.front
            while curr.next!=None:
                curr=curr.next
            curr.next=temp
            self.dequeSize=self.dequeSize+1

    def deleteFront(self):
    
        if self.dequeSize==0:
            return -1
        else:
            temp=self.front
            self.front=self.front.next
            self.dequeSize=self.dequeSize-1
            del temp
        

    def deleteRear(self):
        
        if self.dequeSize==0:
            return -1
        else:
            curr=self.front
            prev=None
            while curr.next!=None:
                prev=curr
                curr=curr.next
            prev.next=curr.next
            self.dequeSize=self.dequeSize-1
            del curr
        

    def getFront(self):
        
        if self.dequeSize==0:
            return -1
        else:
            return self.front.data
        

    def getRear(self):
       
        if self.dequeSize==0:
            return -1
        else:
            curr=self.front
            while curr.next!=None:
                curr=curr.next
            return curr.data
        

    

li = list(map(int, input().split()))
d = Deque()
i=0
while i<len(li):
    if li[i] == -1:
        break
    if li[i]==1:
        d.insertFront(li[i+1])
        i+=2
    elif li[i] == 2:
        d.insertRear(li[i+1])
        i+=2
    elif li[i] == 3:
        d.deleteFront()
        i+=1
    elif li[i] == 4:
        d.deleteRear()
        i+=1
    elif li[i] == 5:
        print(d.getFront())
        i+=1
    elif li[i] == 6:
        print(d.getRear())
        i+=1


