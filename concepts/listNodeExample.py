class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insert(arr):
    node = ListNode(-1)  # Dummy node to simplify list construction
    current = node
    for val in arr:
        current.next = ListNode(val)
        current = current.next

    return node.next