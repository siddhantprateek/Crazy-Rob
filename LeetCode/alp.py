class Solution:
    def shuffle(self, nums: list[int], n: int):
        self.nums = nums
        self.n = n
        size = len(self.nums)

        value_x, value_y = self.nums[:size/2], self.nums[size/2 + 1:size]

        paired_list = list(zip(value_x, value_y))

        for ind, pair in paired_list:
            print(ind, pair)


ret = Solution().shuffle([1, 7, 2, 3, 4, 6], 3)
# numbers = [1, 1, 2, 3, 4, 6]
