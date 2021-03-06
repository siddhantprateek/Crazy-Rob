import math
class Solution:
    def twoSumLessThanK(self, nums: list[int], k: int):
        self.nums = sorted(nums)
        self.k = k 
        value = -1
        for i in range(len(self.nums)):
            for j in reversed(range(len(self.nums))) :
                if (self.nums[i] + self.nums[j] < self.k and i != j):
                    value = max(value, self.nums[i] + self.nums[j])
                
        return print(value)


ret = Solution().twoSumLessThanK([10,20,30], 15)