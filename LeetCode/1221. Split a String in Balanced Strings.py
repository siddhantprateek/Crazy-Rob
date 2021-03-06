# Can anybody explain me why range is inclusive in this case?
class Solution:
    def balancedStringSplit(self, s: str):
        LR = 0
        right = 0
        left = 0
        #  why range argument is inclusing in this case
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                if s[i] == 'L':
                    left += 1
                else:
                    right += 1
            else:
                if s[i] == 'L':
                    left += 1
                else:
                    right += 1
            if left == right:
                LR += 1
        LR += 1
        return LR
