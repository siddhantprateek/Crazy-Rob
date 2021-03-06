class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        
        max_pro = 0
        for i in range(len(nums) - 1):
            for j in range(i, len(nums) - 1):
                current = (nums[i] - 1)*(nums[j + 1] - 1)
                if max_pro < current:
                    max_pro = current 
                
        return max_pro
        