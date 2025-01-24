class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        current_smallest = None

        for letter in letters:
            if letter > target:
                if current_smallest is None or letter < current_smallest:
                    current_smallest = letter

        return current_smallest if current_smallest is not None else letters[0] # this part is cool
