# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        length = 1
        while cur.next:
            cur = cur.next
            length += 1
        cur = dummy
        for i in range(length-n):
            cur = cur.next
        print(cur.val)
        if cur.next:
            cur.next = cur.next.next
        return dummy.next