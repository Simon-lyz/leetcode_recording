# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyhead = ListNode(0)
        dummy = dummyhead
        mark = 0
        while l1 and l2:
            if l1.val + l2.val >= 10:
                dummy.next = ListNode(l1.val + l2.val - 10 + mark)
                mark = 1
            elif l1.val + l2.val + mark == 10:
                dummy.next = ListNode(0)
                mark = 1
            else:
                dummy.next = ListNode(l1.val + l2.val + mark)
                mark = 0
            l1 = l1.next
            l2 = l2.next
            dummy = dummy.next

        while l1:
            if l1.val + mark == 10:
                dummy.next = ListNode(0)
                mark = 1
            else:
                dummy.next = ListNode(l1.val + mark)
                mark = 0
            l1 = l1.next
            dummy = dummy.next

        while l2:
            if l2.val + mark == 10:
                dummy.next = ListNode(0)
                mark = 1
            else:
                dummy.next = ListNode(l2.val + mark)
                mark = 0

            l2 = l2.next
            dummy = dummy.next

        if mark == 1:
            dummy.next = ListNode(1)

        return dummyhead.next