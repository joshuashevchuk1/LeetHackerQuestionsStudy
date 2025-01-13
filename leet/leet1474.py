# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from requests import delete

from concepts.linkedListExample import insertNodeAtTail


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

     def insertAtTail(self, head, data):

         new_node = ListNode(data)

         current = head

         while current.next:
             current = current.next

         current.next = new_node

         return head

     def deleteMatN(self, head ,m,n):
        dn = 1
        current = head
        while current.next:
            if dn != n:
                dn += 1
                current = current.next
            if dn == n:
                dn = 1
                dm = 1
                current = self.deleteM(current,dm)
                current = current.next

     def deleteM(self,node,dm):
         if dm != m:
             dm += 1
             if node.next.next is not None:
                node.next = node.next.next
             return self.deleteM(node,dm)
         return node

     def print(self,head):
        current = head
        while current.next:
            print(current.val)
            current = current.next


# deleteM

# node

# node.next = node.next.next
# node.next = node.next.next.next
# node.next = node.next.next.next.next



a = [1,2,3,4,5,6]
head = ListNode()

for i in range(len(a)):
    head.insertAtTail(head,a[i])

head.print(head)

m = 2
n = 2
head.deleteMatN(head,m,n)

head.print(head)