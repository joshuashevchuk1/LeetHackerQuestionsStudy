# Original
#
# 1. keep a defaultlist called anagrams.
# 2. start with the first str.
# 3. iterate from the first str to the last string.
# 4. if any strs.reverse() are equal append to current array.
# 5. at the end of the strings append to the group array.
# 6. if any string was found in the group array, skip. (they are already grouped.
# 7. now start at i + 1 of the str array and iterate until i = len(strs)
from audioop import reverse


# Refined Plan Using Your Approach:
# 1. Use a visited set to track strings that have already been grouped.
# 2. Start iterating through the array from the first string (i = 0).
# 3. For each string, compare it with all subsequent strings (j = i+1 to len(strs)).
# 4. Check if two strings are anagrams by sorting their characters:
# 5. If sorted(str1) == sorted(str2), they are anagrams, and you group them.
# 6. Skip any string that’s already grouped using the visited set.
# 7. Continue until all strings have been processed.

# Code

def group_anagrams(strs):
    visited = set()  # Keeps track of strings that are already grouped
    anagrams = []    # Stores groups of anagrams

    for i, word in enumerate(strs):
        if word in visited:  # Skip if already grouped
            continue

        group = [word]  # Start a new group
        visited.add(word)  # Mark current word as grouped

        # Compare with all subsequent strings
        for j in range(i + 1, len(strs)):
            if strs[j] not in visited and sorted(word) == sorted(strs[j]):
                group.append(strs[j])  # Add to the group
                visited.add(strs[j])  # Mark as grouped

        anagrams.append(group)  # Add the completed group to the result

    return anagrams

#
# Summary of Key Refinements:
# Aspect	Your Approach	Refined Approach
# Core Check	str.reverse()	sorted(str) for anagram check
# Tracking	Implicit group skipping	Explicit visited set
# Efficiency	O(n^2) with incorrect grouping	O(n^2 * k log k) with correct grouping
# Correctness	Detects palindromes, not anagrams	Correctly groups anagrams

def group_palindromes(strs):
    visited = set()  # Keeps track of strings that are already grouped
    palindromes = []  # Stores groups of palindromes

    for i, word in enumerate(strs):
        if word in visited:  # Skip if already grouped
            continue

        group = [word]  # Start a new group
        visited.add(word)  # Mark current word as grouped

        # Compare with all subsequent strings
        for j in range(i + 1, len(strs)):
            if strs[j] not in visited and word == ''.join(reversed(strs[j])):
                group.append(strs[j])  # Add to the group
                visited.add(strs[j])  # Mark as grouped

        palindromes.append(group)  # Add the completed group to the result

    return palindromes
