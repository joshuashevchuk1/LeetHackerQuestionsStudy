class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def removeFirstNode(head):
    if (head is None):
        return
    head = head.next
    return head


def insertNodeAtHead(head, data):
    new_node = SinglyLinkedListNode(data)
    if head is None:
        return new_node
    else:
        new_node.next = head
        return new_node

def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

def insertNodeAtIndex(head,data,index):
    new_node = SinglyLinkedListNode(data)
    if head is None:
        return new_node
    current = head
    i = 0
    while current.next and i < index - 1:  # Stop at the node before the target index
        current = current.next
        i += 1

    new_node.next = current.next
    current.next = new_node
    return head

def updateNodeAtIndex(head,data,index):
    new_node = SinglyLinkedListNode(data)
    if head is None:
        return new_node
    current = head
    i = 0
    while current.next and i < index:  # Stop at the node at the target index
        current = current.next
        i += 1

    current.data = data

    return head

def removeNodeAtIndex(head,index):
    if head is None:
        return head

    # Special case: Removing the head node
    if index == 0:
        head = head.next
        return head  # New head is the next node

    current = head
    i = 0
    # Traverse to the node just before the target index
    while current is not None and i < index - 1:
        current = current.next
        i += 1

    current.next = current.next.next

    return head


def printNodes(head):
    current = head
    while current:
        print(current.data)
        current = current.next

def getList():
    llist = SinglyLinkedList()
    return llist

def insertAtHeadTest(llist_count):
    llist = getList()

    for i in range(len(llist_count)):
        llist_item = int(llist_count[i])
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head

    printNodes(llist.head)

def insertAtTailTest(llist_count):
    llist = getList()

    for i in range(len(llist_count)):
        llist_item = int(llist_count[i])
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    printNodes(llist.head)

def insertAtIndexTest(llist_count,index):
    llist = makellist(llist_count)
    insertNodeAtIndex(llist.head,4,index)
    printNodes(llist.head)

def updateAtIndextest(llist_count,index):
    llist = makellist(llist_count)
    llist.head = updateNodeAtIndex(llist.head, 4, index)
    printNodes(llist.head)

def removeAtIndextest(llist_count,index):
    llist = makellist(llist_count)
    llist.head = removeNodeAtIndex(llist.head, index)
    printNodes(llist.head)

def removeFirstNodeTest(llist_count):
    llist = makellist(llist_count)
    llist.head = removeFirstNode(llist.head)
    printNodes(llist.head)


def makellist(llist_count):
    llist = getList()

    for i in range(len(llist_count)):
        llist_item = int(llist_count[i])
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head
    return llist


if __name__ == '__main__':
   llist_count = [1,2,3]
   print("make from head")
   insertAtHeadTest(llist_count)
   print("make from tail")
   insertAtTailTest(llist_count)
   print("insert at index")
   insertAtIndexTest(llist_count,2)
   print("update at index")
   updateAtIndextest(llist_count, 3)
   print("remove at index")
   removeAtIndextest(llist_count,0)
   print("remove first node")
   removeFirstNodeTest(llist_count)
