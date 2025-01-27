
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


nums=[1,2,3,4]

def printLinkedList(head):
    current = head
    while current:
        print(current.val)
        current = current.next

def insertNums(nums):
    llist = None
    for num in nums:
        llist = insert(num,llist)
    return llist

# reversing a linked list requires understanding of how to node is being chained

# each item in the node is a linked object that is only broken by if the node is None or not

# the principle of reversing the linked list requires moving around the chain of the list.

# to do this a  pointer method is used.

# a global pointer prev keeps track of the state of the chain.

# the chain is broken by setting to None. because prev hasn't been described yet.

# then saving the state of the next value (BEFORE) breaking the chain allows the current to not immediatly exit the loop.

# the process is repeated until the node is switched around

# Step 1:
#
# p = None
#
# 1 -> 2 ->3 -> None
#
# n = 2 -> 3 -> None
#
# 1 -> None 3 -> None
#
# p = 1 - > None
#
# c = 2 -> 3 -> None
#
# Step 2:
#
# p = 1 - > None
#
# 2 -> 3 -> None
#
# n =  3 -> None
#
# 2 -> 1 -> None
#
# p = 2 -> 1 -> None
#
# c = 3 - > None
#
# Step 3:
#
# 3 -> None
#
# n = None
#
# 3 -> 2 -> 1 -> None
#
# p = 3 -> None
#
# c = None
#
# Loop ends


# keep track of the pointer refs to reverse
def reverseList(head):
    current = head
    prev = None
    while current:
        nnext = current.next # not none
        current.next = prev # None
        prev = current # set prev pointed current val
        current = nnext # set current val to the next val
    return prev

if __name__ == "__main__":
    llist = insertNums(nums)
    printLinkedList(llist)
    llist = reverseList(llist)
    printLinkedList(llist)


