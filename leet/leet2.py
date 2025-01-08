# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        v1 = ""
        v2 = ""

        def rec_l1(l1,v1):
            if l1 is None:
                return v1
            v1 += str(l1.val)
            return rec_l1(l1.next,v1)

        def rec_l2(l2,v2):
            if l2 is None:
                return v2
            v2 += str(l2.val)
            return rec_l2(l2.next,v2)

        v1 = rec_l1(l1,v1)
        v2 = rec_l2(l2,v2)
        v = int(v1) + int(v2)
        vs = list(str(v))
        ra = []
        r = None

        for i in range(len(vs)-1,-1,-1):
            ra = vs[i]

        def insert(node,arr,idx):
            if idx == len(arr)-1:
                return node
            if node is None:
                node = ListNode(arr[idx])
                return insert(node.next,arr,idx + 1)
            node = ListNode(arr[idx])
            return insert(node.next, val, idx + 1)

        r = None
        r = insert(r,ra,0)


# working solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        v1 = ""
        v2 = ""

        def reverse(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev

        l1 = reverse(l1)
        l2 = reverse(l2)

        # Recursive function to build the string for l1
        def rec_l1(l1, v1):
            if l1 is None:
                return v1
            v1 += str(l1.val)
            return rec_l1(l1.next, v1)

        # Recursive function to build the string for l2
        def rec_l2(l2, v2):
            if l2 is None:
                return v2
            v2 += str(l2.val)
            return rec_l2(l2.next, v2)

        # Convert both linked lists to strings
        v1 = rec_l1(l1, v1)
        v2 = rec_l2(l2, v2)

        # Add the two numbers
        v = int(v1) + int(v2)
        vs = list(str(v))  # Split the sum into digits as strings

        # Function to recursively insert values into the linked list
        def insert(node, arr, idx):
            if idx == len(arr):  # Base case: end of list
                return node
            if node is None:
                node = ListNode(int(arr[idx]))  # Create the first node
            else:
                node.next = ListNode(int(arr[idx]))  # Link new node to next
            node.next = insert(node.next, arr, idx + 1)  # Recurse for next element
            return node

        # Initialize the result list and build it using recursion
        r = insert(None, vs, 0)

        # Reverse the result list
        r = reverse(r)

        return r  # Return the reversed linked list