# palindrome of list 
# class Solution:
#     def isPalindrome(self, head: list):   
#         self.head = head
#         joint = ''.join(self.head) 
#         rev_joint = ''.join(reversed(joint))
#         return print(bool(joint == rev_joint))

# ret = Solution().isPalindrome(["a","b","a"])
        
class Solution:
    def isPalindrome(self, head: list):
        self.head = head
        return print(bool(''.join(self.head) == ''.join(reversed(self.head))))

ret = Solution().isPalindrome(["a", "b", "a", "b", "a"])