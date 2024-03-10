# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        lst1 = []
        lst2 = []
        while cur:
            if cur.val >= x:
                lst2.append(cur.val)
            else:
                lst1.append(cur.val)
            cur = cur.next

        cur = dummy
        while lst1:
            cur.next = ListNode(lst1.pop(0))
            cur = cur.next
        while lst2:
            cur.next = ListNode(lst2.pop(0))
            cur = cur.next

        return dummy.next

