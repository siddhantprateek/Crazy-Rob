class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]):
        merged = sorted(nums1 + nums2)
        length_merged = len(merged)
        if(length_merged % 2 == 0):
            median = (merged[int(length_merged/2-1)] +
                      merged[int(length_merged/2)])/2
        else:
            median = merged[int((length_merged - 1)/2)]

        return median


ret = Solution().findMedianSortedArrays([1, 2], [3, 4])
# Took 289ms
