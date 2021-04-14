class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        return self.isScrambled(s1, s2)

    def isScrambled(self, s1, s2, freq = {}):

        if len(s1) != len(s2) and sorted(s1) != sorted(s2):
            return False

        # if only single character is present is only present
        if len(s1) <= len(s2) <= 1:
            return s1 == s2

        if (s1, s2) in freq:
            return freq[s1,s2]

        n = len(s1)
        for i in range(1, n):
            temp1 = self.isScrambled(s1[:i], s2[:i], freq) and self.isScrambled(s1[i:], s2[i:], freq)

            if not temp1:
                temp2 = self.isScrambled(s1[:i], s2[-i:], freq) and self.isScrambled(s1[i:], s2[:-i], freq)

            if temp1 or temp2:
                freq[s1, s2] = True
                return True

        freq[s1, s2] = False
        return False

sol = Solution().isScrambled("great", "rgeat")
print(sol)

