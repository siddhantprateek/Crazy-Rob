# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Follow up: Could you do this in one pass?

# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        if head is None:
            return None

        else:
            NodeLength = self.getLength(head)

            Nodepos = NodeLength - n -1
            temp = head

            if n == NodeLength:
                return head.next

            while Nodepos != 0:
                temp = temp.next
                Nodepos -= 1
            if temp is not None:
                temp.next = temp.next.next
            return head


    def getLength(self, head):
        temp = head
        length = 0
        while temp is not None:
            length += 1
            temp = temp.next
        return length
