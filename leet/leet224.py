# 1st solution
class Solution:
    def calculate(self, s: str) -> int:
        s = self.removeSpaces(s)  # Remove all whitespaces
        result, _ = self.process_expr(s, 0)  # Get the result from the expression
        return result

    def removeSpaces(self, s):
        return s.replace(" ", "")

    def process_expr(self, s, idx):
        result = 0
        sign = 1  # 1 for positive, -1 for negative
        while idx < len(s):
            if s[idx] == "(":
                idx += 1  # Skip the '('
                sub_result, idx = self.process_expr(s, idx)  # Recursively process inside parentheses
                result += sign * sub_result
            elif s[idx] == ")":
                return result, idx + 1  # End of current parentheses, return result

            elif s[idx] == "+":
                sign = 1  # Next number should be positive
                idx += 1
            elif s[idx] == "-":
                sign = -1  # Next number should be negative
                idx += 1
            elif self.can_convert_to_int(s[idx]):
                num, idx = self.process_number(s, idx)  # Process the current number
                result += sign * num
            else:
                idx += 1  # Skip any non-relevant characters

        return result, idx  # Return the result and current index

    def process_number(self, s, idx):
        # Process a number starting at index idx
        num = 0
        while idx < len(s) and self.can_convert_to_int(s[idx]):
            num = num * 10 + int(s[idx])
            idx += 1
        return num, idx

    def can_convert_to_int(self, char):
        return char.isdigit()

# without recursion solution

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_num = 0
        sign = 1  # 1 for positive, -1 for negative
        result = 0
        idx = 0

        while idx < len(s):
            char = s[idx]

            if char.isdigit():
                current_num = current_num * 10 + int(char)  # Build the current number
            elif char == "+":
                result += sign * current_num  # Add the current number with the correct sign
                current_num = 0  # Reset current number
                sign = 1  # Set sign to positive for the next number
            elif char == "-":
                result += sign * current_num  # Add the current number with the correct sign
                current_num = 0  # Reset current number
                sign = -1  # Set sign to negative for the next number
            elif char == "(":
                # Push the result and sign onto the stack and reset them for the new subexpression
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ")":
                # Pop the sign and result from the stack and apply the result
                result += sign * current_num
                current_num = 0
                result *= stack.pop()  # Apply the sign before the parentheses
                result += stack.pop()  # Add the result before the parentheses

            idx += 1

        result += sign * current_num  # Add the last number
        return result