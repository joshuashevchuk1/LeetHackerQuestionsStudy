# original

# 0. have a pointer for the longest string
# 1. have a heap/queue called current that determines the current longest substring.
# 2. have a recursion at j where the recursion doesn't end until  starting = len(str)
# 3. for i in range(len): add the current strings togther with the heap until str(j) = str(j+1).
# 3b. once the condition is meet the longest string pointer becomes the current string
# 4. now keep track of starting a starting = j.
# 5. recurse on the next part of the array and if the current string is greater then the longest string, set the longest string to the current string.
# 6. iterate until the array is finished



# code

# faster because sliding window is in O(n)
def length_of_longest_substring(s):
    char_map = {}  # Keeps track of the most recent index of characters
    left = 0  # Left pointer of the window
    max_len = 0  # Stores the length of the longest substring

    for right in range(len(s)):
        # If the character is in the window and its index is >= left, adjust left pointer
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1  # Move left to the right of the previous occurrence

        # Update the character's last seen index in char_map
        char_map[s[right]] = right

        # Calculate the current window length and update max_len
        max_len = max(max_len, right - left + 1)

    return max_len


import heapq

# heap is slower than a sliding window O(n log(n))
def length_of_longest_substring(s):
    char_map = {}  # Keeps track of the most recent index of characters
    left = 0  # Left pointer of the window
    max_len = 0  # Stores the length of the longest substring
    heap = []  # Min-heap to store lengths of substrings

    for right in range(len(s)):
        # If the character is in the window and its index is >= left, adjust left pointer
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1  # Move left to the right of the previous occurrence
        # Update the character's last seen index in char_map
        char_map[s[right]] = right
        # Calculate the current window length
        current_len = right - left + 1
        # Push the current length into the heap
        heapq.heappush(heap, current_len)
        # Update max_len to ensure it's the longest length
        max_len = max(max_len, current_len)

    return max_len

# conclusion, use a sliding window

# Step 1: Initialize variables
# - Create a dictionary to track the most recent index of characters (char_map)
# - Initialize two pointers: left (start of the window), right (end of the window)
# - Initialize max_len to store the length of the longest substring found

# Step 2: Iterate through the string with the 'right' pointer
# - Move 'right' pointer through the entire string

# Step 3: Check if the current character is in the window
# - If the character at s[right] is already in the window and its index is >= left
# - It means we have a repeated character within the current window

# Step 4: Adjust the 'left' pointer to remove the duplicate
# - Move 'left' to the position right after the last occurrence of s[right]
# - This ensures the window contains only unique characters

# Step 5: Update the character map
# - Update the last seen index of s[right] in the char_map

# Step 6: Calculate the current window length
# - Current window length is (right - left + 1)

# Step 7: Update the max_len if necessary
# - If the current window length is larger than max_len, update max_len

# Step 8: Continue until the 'right' pointer has processed all characters in the string

# Step 9: Return the result
# - Return the value of max_len, which holds the length of the longest substring without repeating characters

