

class Solution:
    def strongPasswordChecker(self, password):
        self.password = password

        char = self.password
        num = list(range(10))
        if len(self.password) >= 8:
            if num and ord(char) >= 65 and ord(char) <= 90 and ord(char) >= 97 and ord(char) <= 122 in self.password:
                print("strong")
            else:
                print("weak")
        else:
            print("re-enter")


passval = Solution()
passval.strongPasswordChecker("456Amaquit")
