class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # To keep track of strings and multipliers
        current_string = ""  # Current decoded string
        current_num = 0  # Multiplier for the current level

        for char in s:
            if char.isdigit():
                # Build the multiplier (in case it's more than one digit)
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current string and multiplier onto the stack
                stack.append((current_string, current_num))
                # Reset for the new substring
                current_string = ""
                current_num = 0
            elif char == ']':
                # Pop the last string and multiplier from the stack
                last_string, multiplier = stack.pop()
                # Decode the current level and concatenate with the last level
                current_string = last_string + current_string * multiplier
            else:
                # Build the current string
                current_string += char

        return current_string
