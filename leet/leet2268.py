# TODO: solve me
#
# 2268 : minimum number of key presses
#
# You have a keypad with 9 buttons, numbered from 1 to 9, each mapped to lowercase English letters.
# You can choose which characters each button is matched to as long as:
#
# All 26 lowercase English letters are mapped to.
# Each character is mapped to by exactly 1 button.
# Each button maps to at most 3 characters.
# To type the first character matched to a button, you press the button once.
# To type the second character,
# you press the button twice, and so on.
#
# Given a string s, return the minimum number of keypresses needed to type
# s using your keypad.
#
# Note that the characters mapped to by each button, and the order they are mapped in cannot be changed.
#
#
# Since you have control over the number of presses the answer is just
# 1. sort lexio-graphically.
# 2. assign the 1st 9 to a set with multiplier 1
# 3. assign the 2nd 9 to a set with multiplier 2
# 4. assign the last 9 to a set with multiplier 3.
# 5. For each char in the string, find it in the 3 arrays and then its multiplier.
# 6. to do this quickly, assign key press as a dict whose value is multiplier and key is the char.
# 7. then O(1) on the dict, and add so O(1) + O(n) and the calc time is O(n log(n)) (due to the sorting step).

from collections import defaultdict, Counter


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        def get_sorted_string(s):
            # Sort characters by frequency (descending), then alphabetically
            freq = Counter(s)
            sorted_string = sorted(freq.keys(), key=lambda x: (-freq[x], x))
            return ''.join(sorted_string)

        def getMultipliers(key_grid):
            multipliers = defaultdict(list)
            total_length = len(key_grid)

            if total_length > 0:
                multipliers[1] = key_grid[:9]  # First 9 characters
            if total_length > 9:
                multipliers[2] = key_grid[9:18]  # Next 9 characters
            if total_length > 18:
                multipliers[3] = key_grid[18:]  # Remaining characters

            return multipliers

        sorted_string = get_sorted_string(s)
        weights = getMultipliers(sorted_string)

        total_presses = 0

        for char in s:
            if char in weights[1]:
                total_presses += 1
            elif char in weights[2]:
                total_presses += 2
            elif char in weights[3]:
                total_presses += 3

        return total_presses

# faster solution
class SolutionBetter: # T # O (n + k log (k))
    def minimumKeypresses(self, s: str) -> int:
        # Count frequency of each character
        freq = Counter(s)

        # Sort characters by frequency (descending), then alphabetically
        sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

        # Assign weights directly based on position
        total_presses = 0
        for i, (char, count) in enumerate(sorted_chars):
            weight = i // 9 + 1  # Group 1: 0-8, Group 2: 9-17, Group 3: 18-26, etc.
            total_presses += weight * count

        return total_presses

