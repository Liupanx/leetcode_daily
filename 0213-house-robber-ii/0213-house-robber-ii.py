class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        return max(self.circle_rob(nums[:-1]), self.circle_rob(nums[1:]))

    def circle_rob(self, nums):
        n1, n2 = 0, 0
        n = len(nums)
        
        for num in nums:
            temp = max(n1, n2)
            n1 = max(n1, n2 + num)
            n2 = temp
        return max(n1, n2)
    

