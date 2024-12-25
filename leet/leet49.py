from collections import defaultdict
import numpy as np
import string


class AnagramCalculator:
    def __init__(self, count, size):
        self.count = count  # Number of words to generate
        self.size = size    # Size of each word (number of letters)

    def groupAnagrams(self, strs):
        """
        Groups strings into anagrams.
        :param strs: List of strings
        :return: List of grouped anagrams
        """
        anagrams = defaultdict(list)
        for string in strs:
            sorted_string = ''.join(sorted(string)) # O(k log(k))
            anagrams[sorted_string].append(string)
        return list(anagrams.values())

    def makeWordArray(self):
        """
        Generates an array of random words.
        :return: List of random words
        """
        letters = list(string.ascii_lowercase)
        lettersArray = []
        for _ in range(self.count):
            # Ensure `self.size` does not exceed the alphabet length if `replace=False`
            random_selection = np.random.choice(letters, size=min(self.size, len(letters)), replace=False)
            word = ''.join(random_selection)
            lettersArray.append(word)
        return lettersArray

    def discoverAnagrams(self):
        """
        Generates random words and counts the number of anagram groups.
        :return: None
        """
        # Generate the word array
        letterArray = self.makeWordArray()

        # Group anagrams
        all_results = self.groupAnagrams(letterArray)

        # Count the number of anagram groups with more than one word
        number_of_anagrams = sum(1 for group in all_results if len(group) > 1)
        print(f"Number of anagram groups with more than one word: {number_of_anagrams}")


# Example usage
count = int(1e6)  # Number of words to generate
size = 20         # Size of each word

ang_cal = AnagramCalculator(count, size)
ang_cal.discoverAnagrams()
