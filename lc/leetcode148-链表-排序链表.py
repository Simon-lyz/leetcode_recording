# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l = []
        p = head
        while p:
            l.append(p.val)
            p = p.next

        s_l = sorted(l)
        dummy = ListNode(0)
        p = dummy
        for e in s_l:
            p.next = ListNode(e)
            p = p.next

        return dummy.next