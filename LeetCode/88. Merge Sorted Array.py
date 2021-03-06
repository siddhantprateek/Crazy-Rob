class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int):
        self.nums1 = nums1
        self.m = m
        self.nums2 = nums2
        for i in range(self.nums1.count(0)):
            self.nums1.remove(0)
        for i in range(self.nums2.count(0)):
            self.nums2.remove(0)

        result = "".join(self.nums2, self.nums1)
        return print(sorted(self.nums1))


ret = Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
