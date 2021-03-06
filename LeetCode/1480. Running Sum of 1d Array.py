"""
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums.
    
    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
"""


class Solution:
    def runningSum(self, nums: list[int]):
        self.nums = nums
        result_list = []
        for i in range(len(self.nums)):
            result_list.append(sum(self.nums[:i+1]))
        return print(result_list)


ret = Solution().runningSum([1, 2, 3, 4])
