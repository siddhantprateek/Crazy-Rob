class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]):
        self.word1 = word1
        self.word2 = word2

        return print(''.join(self.word1) == ''.join(self.word2))


ret = Solution().arrayStringsAreEqual(["ab", "c"], ["a", "bc"])
