# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        k %= length
        if k == 0:
            return head

        cur = dummy
        for i in range(length - k):
            cur = cur.next

        new_head = cur.next
        cur.next = None

        dummy2 = ListNode(0)
        dummy2.next = new_head
        for i in range(k - 1):
            new_head = new_head.next

        new_head.next = dummy.next
        return dummy2.next



