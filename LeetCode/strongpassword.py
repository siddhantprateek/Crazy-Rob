class Solution:
    def strongPasswordChecker(self, password: str):
        self.password = password

        length = len(self.password)

        if length < 6:
            return print(6-length)
        return print(0)


ret = Solution().strongPasswordChecker("aaa123")
