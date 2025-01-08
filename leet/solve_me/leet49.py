# 1. Use a visited set to track strings that have already been grouped.
# 2. Start iterating through the array from the first string (i = 0).
# 3. For each string, compare it with all subsequent strings (j = i+1 to len(strs)).
# 4. Check if two strings are anagrams by sorting their characters:
# 5. If sorted(str1) == sorted(str2), they are anagrams, and you group them.
# 6. Skip any string that’s already grouped using the visited set.
# 7. Continue until all strings have been processed.

