class Solution(object):
    def addTwoNumbers(self, l1, l2):
        returnList = ListNode(0)
        r = returnList
        p1, p2 = l1, l2
        remainder = 0

        while p1 or p2:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0

            mySum = v1 + v2 + remainder
            r.next = ListNode(mySum % 10)
            remainder = mySum // 10
            r = r.next

            if p1: p1 = p1.next
            if p2: p2 = p2.next

        if remainder:
            r.next = ListNode(remainder)

        return returnList.next
