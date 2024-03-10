# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return None

        cnt = 0
        cur = head
        while cur:
            cur = cur.next
            cnt += 1
        if cnt - n - 1 < 0:
            return head.next

        cur = head
        for i in range(cnt - n - 1):
            cur = cur.next

        pre = cur
        nxt = cur.next
        pre.next = nxt.next
        nxt.next = None
        return head