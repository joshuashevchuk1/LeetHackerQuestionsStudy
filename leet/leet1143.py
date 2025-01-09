

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # Initialize dp table with zeros
        dp = [[0] * (n + 1) for _ in range(m + 1)] # this concept is needed.

        # these dp always fill this way. it solves the problem due to overlapping subproblems and only a count is needed
        print(dp)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:  # Characters don't match
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        print(dp)
        return dp[m][n]



solution = Solution()
print(solution.longestCommonSubsequence("abcde","ace"))