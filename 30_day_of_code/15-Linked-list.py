class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
    
        node = Node(data)
        if head==None:
            return node
        else:
            current = head
            while current.next != None:
                current = current.next
            current.next = node
            return head

mylist= Solution()
head = None
n = int(input())
for i in range(n):
    data = int(input())
    head = mylist.insert(head,data)
mylist.display(head)