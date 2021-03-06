from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]):
        self.nums = nums      
        majority = 1
        # for x in self.nums:
        #     majority = max(majority, self.nums.count(x))
        # return print(majority)    
        
        new_list = Counter(self.nums)
        print(new_list)

        for key, value in new_list.items():
            min_ = value
            if 


ret = Solution().majorityElement([2,2,1,1,1,2,2])