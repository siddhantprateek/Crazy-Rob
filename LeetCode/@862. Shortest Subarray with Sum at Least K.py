"""
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.
If there is no non-empty subarray with sum at least K, return -1.
Example 1:
Input: A = [1], K = 1
Output: 1
Example 2:
Input: A = [1,2], K = 4
Output: -1
Example 3:
Input: A = [2,-1,2], K = 3
Output: 3

Note:
1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9
"""

class Solution:
    def shortestSubarray(self, A: list[int], K: int):
        
        sum_ = 0
        # for i in range(len(A)):
        # loop over and compare the sums
            # sum_ += A[i]
        for i in range(len(A)-1):
            sum_ = A[i] 
            for j in range(i+1, len(A)-1):
                if sum_ == K:
                    return print(len(A))
                sum_ += A[j]
        return print(-1)
        # if sum_ == K:
        #     return print(K)
        # else:
        #     return print(-1)
    
ret = Solution().shortestSubarray([77,19,35,10,-14], 19)
# Wrong Answer
# Details 
# Input
# [77,19,35,10,-14]
# 19
# Output
# -1
# Expected
# 1