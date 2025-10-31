class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Approach 1
        # if len(nums) == 1:
        #     return True

        # goal = len(nums)-1

        # for i in range(len(nums)-1,-1,-1):
        #     if i + nums[i] >= goal:
        #         goal = i
        # return goal == 0

         #Approach 2
        if len(nums) == 1:
            return True
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(i+nums[i], max_reach)
            if max_reach >= len(nums)-1:
                return True




