# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyhead = ListNode(0)
        dummyhead.next = head
        cur = dummyhead
        nxt = head

        while cur and nxt:
            node1 = cur.next
            node2 = cur.next.next

            # 交换
            node1.next = node2.next
            cur.next = node2
            node2.next = node1

            cur = node1

        return dummyhead.next