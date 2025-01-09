from num2words import num2words

# not a really good problem

# realistic solution
class Solution:
    def numberToWords(self, num: int) -> str:
        return num2words(num)


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        # Lists for digits, tens, and powers of thousand
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
                "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return ones[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return ones[n // 100] + " Hundred " + helper(n % 100)

        result = ""
        thousand_idx = 0

        while num > 0:
            if num % 1000 != 0:
                result = helper(num % 1000) + thousands[thousand_idx] + " " + result
            num //= 1000
            thousand_idx += 1

        return result.strip()