from typing import List, Any


class Solution:
    def get_len_lcs(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # Initialize dp table with zeros
        dp = [[0] * (n + 1) for _ in range(m + 1)] # this concept is needed.

        # these dp always fill this way. it solves the problem due to overlapping subproblems and only a count is needed
        print(dp)
        dp = self._get_dp(dp, m, n, text1, text2)
        print(dp)
        return dp[m][n]

    def get_lcs_elements(self, text1: str, text2: str) -> list[Any]:
        m, n = len(text1), len(text2)
        # Initialize dp table with zeros
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # this concept is needed.

        # these dp always fill this way. it solves the problem due to overlapping subproblems and only a count is needed
        print(dp)
        dp = self._get_dp(dp, m, n, text1, text2)
        result = self._fill_lcs(dp,m,n,text1,text2)
        return result

    def _get_dp(self, dp, m, n, a, b):
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:  # Characters don't match
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp


    def _fill_lcs(self, dp, m, n, a, b):
        i = m
        j = n
        result = []
        while i > 0 and j > 0:
            if a[i-1] == b[j-1]:
                result.append(a[i-1])
                i -= 1
                j -= 1
            elif dp[i][j-1] >=  dp[i-1][j]:
                j -= 1
            else:
                i -= 1
        result.reverse()
        return result

text1="abcdesefsefsad"
text2="acedesfsefsfde"
solution = Solution()
lcs = solution.get_len_lcs(text1, text2)
print(lcs)
result = solution.get_lcs_elements(text1,text2)
print(result)