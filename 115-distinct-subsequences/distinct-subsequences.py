class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(t)

        # dp[j] = number of ways to form t[:j]
        dp = [0] * (m + 1)

        # Empty string t can always be formed in 1 way
        dp[0] = 1

        for ch in s:
            # Traverse backwards
            for j in range(m, 0, -1):
                if ch == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[m]
        