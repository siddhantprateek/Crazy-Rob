class Solution:
    def mergeKLists(self, lists: list[list]):
        self.lists = lists
        new_lists = []
        for char in self.lists:
            new_lists += char
        return print(sorted(new_lists))


ret = Solution().mergeKLists([])


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         self.nodes = []
#         head = point = ListNode(0)
#         for l in lists:
#             while l:
#                 self.nodes.append(l.val)
#                 l = l.next
#         for x in sorted(self.nodes):
#             point.next = ListNode(x)
#             point = point.next
#         return print(head.next)


# ret = Solution().mergeKLists([[1, 4, 5], [1, 3, 4], [2, 6]])
