class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s) + 1
        dp = [False] * n
        dp[0] = True

        for i in range(n):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    
        return dp[-1]

        # n = len(wordDict)
        # count = 0
        # for word in wordDict:
        #     if word in s:
        #         count += 1
        #     else:
        #         count += 0
        # return count == n
