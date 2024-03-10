class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        cur = dummy
        cur1,cur2 = list1,list2
        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur.next = cur1
                cur = cur.next
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur = cur.next
                cur2 = cur2.next

        while cur1:
            cur.next = cur1
            cur = cur.next
            cur1 = cur1.next
        while cur2:
            cur.next = cur2
            cur = cur.next
            cur2 = cur2.next

        return dummy.next