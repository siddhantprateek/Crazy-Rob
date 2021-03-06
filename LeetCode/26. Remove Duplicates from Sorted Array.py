class Solution:
    def removeDuplicates(self, nums: list[int]):
        result = []
        for i in nums:
            if i not in result:
                result.append(i)
        return str(result)
