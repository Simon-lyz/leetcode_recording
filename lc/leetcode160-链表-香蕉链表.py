# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        cntA = 0
        tmphA = headA
        tmphB = headB
        while tmphA.next != None:
            cntA += 1
            tmphA = tmphA.next
        cntB = 0
        while tmphB.next != None:
            cntB += 1
            tmphB = tmphB.next

        if cntA < cntB:
            for i in range(cntB - cntA):
                headB = headB.next
        else:
            for i in range(cntA - cntB):
                headA = headA.next

        while headA != None and headB != None:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next

        return None