# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4^x.
import math
import cmath

class Solution:
    def isPowerOfFour(self, n: int):
        self.n  = n
        # isinstance(n, int) to check wheather it belong to integer class
        #value = str((math.log(self.n, 4))
        # check wheather float is whole number
        if self.n > 0:
            return print((math.log(self.n, 4)).is_integer())
        else:
            self.n = -self.n
            return print((-math.log(self.n, 4)).is_integer())

ret = Solution().isPowerOfFour(-4)


# 4^x x: 0   1     2    3    4     5   6   7
#     n: 1   4    16   64   256...

# x = log4(number)