class Solution:
    def kthCharacter(self, k: int) -> str:

        s = ["a"]

        def next_letter(char):
            return chr(ord(char) + 1)

        while len(s) < k:
            for i in range(len(s)):
                s.append(next_letter(s[i]))

        return s[k - 1]

# que method

from collections import deque

class Solution:
    def kthCharacter(self, k: int) -> str:
        # Initialize the deque with the first character ('a')
        dq = deque(['a'])

        # We keep processing until the deque contains the required number of characters
        while len(dq) < k:
            current_size = len(dq)
            for _ in range(current_size):
                char = dq.popleft()  # Get the first character in the deque
                dq.append(char)  # Append it again (doubling the sequence)
                dq.append(chr(ord(char) + 1))  # Append the next letter after current character

        return dq[k - 1]  # Return the k-th character, 1-indexed


# non brture force, but O(K) still
from collections import deque

class Solution:
    def kthCharacter(self, k: int) -> str:
        dq = deque(['a'])

        while len(dq) < k:
            current_size = len(dq)
            for _ in range(current_size):
                char = dq.popleft()
                dq.append(char)
                dq.append(chr(ord(char) + 1))

        return dq[k - 1]


# O(1) obscure solution using ascii count

# this is called a bitwise operation and it is the most efficient here.

# its a pretty solution but not the most obvious

from string import ascii_lowercase

class Solution:
    def kthCharacter(self, k: int) -> str:
        return ascii_lowercase[(k-1).bit_count()]