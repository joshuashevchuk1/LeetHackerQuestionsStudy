# TODO: Solve me
#
# 330. Valid Palindrome IV
# Medium
# Topics
# Companies
# Hint
# You are given a 0-indexed string s consisting of only lowercase English letters.
# In one operation, you can change any character of s to any other character.
#
# Return true if you can make s a palindrome after performing exactly one or two operations, or return false otherwise.

# Conceptual plan
#
# Iterate over the string:
#
# Use two pointers, i starting from the left (0) and j starting from the right (len(s) - 1).
# Check for mismatch:
#
# If the characters at positions i and j are not the same, we attempt to make a palindrome by skipping one of the characters:
# Skip the character at i and check if the substring between i+1 and j is a valid palindrome.
# Skip the character at j and check if the substring between i and j-1 is a valid palindrome.
# Return True:
#
# If no mismatch occurs during the iteration, or if one of the skipped cases results in a valid palindrome, return True.
# Helper function:
#
# is_valid checks whether two characters at the given positions are the same.
