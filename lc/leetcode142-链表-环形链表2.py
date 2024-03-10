2# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list1 =[]
        cur = head
        while cur != None and cur.val not in list1:
            list1.append(cur.val)
            cur = cur.next

        if cur == None:
            return False
        else:
            return True