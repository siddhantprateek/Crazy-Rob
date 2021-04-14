class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:

        return self.maximum(nums, 0)

    def maximum(self, nums, index):

        if index == len(nums):
            return 0


