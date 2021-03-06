class Solution:
    def moveZeroes(self, nums: list[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        self.nums = sorted(nums)
        no_of_zeros = self.nums.count(0)
        for i in range(no_of_zeros):
            self.nums.remove(0)

        for i in range(no_of_zeros):
            self.nums.append(0)

        return print(self.nums)


ret = Solution().moveZeroes([0, 1, 0, 3, 12])
