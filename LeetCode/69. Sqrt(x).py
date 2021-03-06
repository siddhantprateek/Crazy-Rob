import math


class Solution:
    def mySqrt(self, x: int):
        self.x = x
        # r = math.sqrt(self.x)
        return print("{:.0f}".format(math.sqrt(self.x)//1))

        # "{:.0f}".format is used remove decimal places or GIF of x
ret = Solution().mySqrt(8)


class Solution:
    def isPowerOfFour(self, n: int):
        self.n = n

        if self.n > 0:
            # check wheather float is whole number
            return (math.log(self.n, 4)).is_integer()
        elif self.n < 0:
            self.n = -self.n
            # check wheather float is whole number
            return (-math.log(self.n, 4)).is_integer()
        else:
            return False
