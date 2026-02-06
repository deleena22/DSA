# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next # 1 jump
            fast = fast.next.next # 2 jumps

            if fast == slow:
                return True
        
        return False

        