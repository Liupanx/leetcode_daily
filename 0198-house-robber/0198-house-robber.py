class Solution:
    def rob(self, nums: List[int]) -> int:
        # method 1
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

        # method 2 
        # dp = [0] * (n)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # for i in range(2, n):
        #     dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        # return dp[-1]
        
