"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].
Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

"""


class Solution:
    def shuffle(self, nums: list[int], n: int):
        self.nums = nums
        self.n = n

        combine_xy = []
        for i in range(self.n):
            combine_xy.append(self.nums[i])
            combine_xy.append(self.nums[self.n + i])

        return print(combine_xy)


ret = Solution().shuffle([2, 5, 1, 3, 4, 7], 3)
