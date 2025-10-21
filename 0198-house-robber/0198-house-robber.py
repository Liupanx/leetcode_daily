class Solution:
    def rob(self, nums: List[int]) -> int:
        # method 1 fib 
        prev, prev_prev = 0, 0

        for money in nums:
            new = max(prev, prev_prev + money)
            prev_prev = prev
            prev = new
        return prev
        

        # method 2 dp 
        # dp = [0] * (n)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # for i in range(2, n):
        #     dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        # return dp[-1]
        
