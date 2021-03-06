class Solution:
    def twoSum(self, nums: list[int], target: int):
        self.nums = nums
        self.target = target
        index = []
        for i in range(len(self.nums)):
            for j in range(i+1, len(self.nums)):
                if (self.nums[j] == self.target - self.nums[i]):
                    index.append(i)
                    index.append(j)
                    return print(list(index))
                # if self.nums[j] == target:
                #     index.append(j)
                #     return print(list(index))

        return print(list(index))


ret = Solution().twoSum([-10, -1, -18, -19], -19)
