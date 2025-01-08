class Solution:
    def isValid(self, s: str) -> bool:
        n_paren = False
        n_bracket = False
        n_squigle = False
        for char in s:
            n_paren =   self.setNeeds_paren(char,n_paren)
            n_bracket = self.setNeeds_bracket(char, n_bracket)
            n_squigle = self.setNeeds_squigle(char, n_squigle)

        if n_paren or n_bracket or n_squigle:
            return False

        return True

    def setNeeds_paren(self,char, needs):
        if char == "(":
           needs = True
        if needs and char == ")":
            needs = False
        return needs

    def setNeeds_bracket(self,char,needs):
        if char == "[":
            needs = True
        if needs and char == "]":
            needs = False
        return needs

    def setNeeds_squigle(self,char,needs):
        if char == "{":
            needs = True
        if needs and char == "}":
            needs = False
        return needs


# better solution

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in "({[":
                stack.append(char)
            elif char in ")}]":
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()

        return not stack
