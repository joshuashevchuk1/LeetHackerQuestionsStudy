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

