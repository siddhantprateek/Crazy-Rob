# class Solution:
#     def reorganizeString(self, s: str):
#         self.s = s

#         for i in range(len(self.s)):
#             if self.s[i] != self.s[i-1]:
#                 self.s[i - 1], self.[i - 2] = self.s[i - 2], self.s[i - 1]
#                 if self.s[i] != self.s[i-1]:
