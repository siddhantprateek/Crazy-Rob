"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Example 1:
Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15
"""
# can be done be putting all the number in a list


class Solution:
    def subtractProductAndSum(self, n: int):
        self.n = n
        n_product = 1
        n_sum = 0
        power = len(str(self.n)) - 1
        while power >= 0:  # it will run until power becomes zero
            # if self.n become zero before "power", which means n_product must be zero
            # so block must run until power becomes zero
            n_sum = n_sum + self.n//10**power
            n_product = n_product*(self.n//10**power)
            self.n = self.n % 10**power
            power -= 1
        return print(n_product - n_sum)


ret = Solution()
ret.subtractProductAndSum(234)
# print(isinstance(ret, Solution))
