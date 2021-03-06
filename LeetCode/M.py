class Solution:
    def multiply(self, num1: str, num2: str):
        self.num1 = int(num1)
        self.num2 = int(num2)

        num = self.num1*self.num2
        return print(str(num))


ret = Solution().multiply("2", "3")
