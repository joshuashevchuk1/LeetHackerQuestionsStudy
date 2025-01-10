# Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.
#
# Return the minimum number of substrings in such a partition.
#
# Note that each character should belong to exactly one substring in a partition.

"""
Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
"""

"""
Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").
"""

def getMinimumPartitions(string):
    """
    :param string:
    :return:
    """
    current_set = set()
    sets = []

    for char in string:
        if char in current_set and char not in sets:
            current_set.clear()
            sets.append(current_set)
        current_set.add(char)

    print(sets)
    return len(sets)+1


def getMinimumPartitionsV2(string):
    """
    :param string:
    :return:
    """
    partition_count = 1  # Start with one partition
    current_set = set()  # Set to track unique characters in the current substring

    for char in string:
        if char in current_set:
            # Start a new partition if the character is already in the current set
            partition_count += 1
            current_set.clear()  # Clear the set to start a new partition
        current_set.add(char)  # Add the character to the current partition

    return partition_count

class Solution:
    def partitionString(self, s: str) -> int:
        """
        :param s:
        :return:
        """
        sub = ""
        num = 0
        for i in s:
            if i in sub:
                sub = i
                num +=1
            else:
                sub += i
        return num+1

string ="abacaba"
print(getMinimumPartitions(string))
print(getMinimumPartitionsV2(string))
solution = Solution()
print(solution.partitionString(string))