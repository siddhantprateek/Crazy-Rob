# class Solution:
#     def shortestDistance(self, words: list[str], word1: str, word2: str):
#         self.words = words
#         self.word1 = word1
#         self.word2 = word2

#         for i in range(len(self.words)):
#             index_of_word1 = index(self.word1) 
#             index_of_word2 = index(self.word2) 

#         # if self.word1 and self.word2 in self.words:
#         #     distance = abs(self.words.index(self.word2) -
#         #                    self.words.index(self.word1))

#         #     return print(distance)
#         # else:
#         #     return print("Element not found")


# ret = Solution().shortestDistance(
#     ["practice", "makes", "perfect", "coding", "makes"], "coding", "practice")

# # except (ValueError):
# #     print("Element not found")
class Solution:
    def shortestDistance(self, words: list[str], word1: str, word2: str):
        self.words = words
        self.word1 = word1
        self.word2 = word2
        distance = len(self.words)
        for i in range(len(self.words)):
            if self.words[i] == self.word1:
                for j in range(len(self.words)):
                    if self.words[j] == self.word2:
                        distance = min(distance, abs(i - j))
        return print(distance)


ret = Solution().shortestDistance(
    ["practice", "makes", "perfect", "coding", "makes"], "coding", "makes")