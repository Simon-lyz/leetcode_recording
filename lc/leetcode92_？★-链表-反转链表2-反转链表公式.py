# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # reverse
        dummyhead = ListNode(-1)
        dummy = dummyhead
        dummy.next = head
        for i in range(left - 1):
            dummy = dummy.next

        cur = dummy.next
        for i in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = dummy.next
            dummy.next = temp
        return dummyhead.next



