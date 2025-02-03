from sqlalchemy.sql.functions import current_time


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insert(val, head):
    node = Node(val)
    if head is None:
        return node

    current = head
    while current.next:
        current = current.next

    current.next = node

    return head

nums = [1,2,3,4]

def revsereList(head):
    current = head
    prev = None

    while current:
        nnext = current.next
        current.next = prev
        prev = current
        current = nnext

    return prev

def insertAtTail(val,head):
    node = Node(val)

    if head is None:
        return node

    current = head
    while current.next:
        current = current.next

    current.next = node

    return head

def insertAtHead(val, head):
    node = Node(val)
    node.next = head
    return node