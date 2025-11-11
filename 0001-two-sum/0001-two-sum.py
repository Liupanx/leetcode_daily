class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compl = {}
        res = []
        n = len(nums)

        for i in range(n):
            compl[nums[i]] = i
        
        for i in range(n):
            complement = target - nums[i]
            if complement in compl and i != compl[complement]:
                return [i, compl[complement]]
        
        return []

            