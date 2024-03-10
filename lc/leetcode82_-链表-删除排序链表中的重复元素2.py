# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        import collections
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        cur = head


        lst = []
        while cur:
            lst.append(cur.val)
            cur = cur.next
        res = collections.Counter(lst)
        print(res)
        cur = dummy
        while cur.next:
            if res[cur.next.val] > 1:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


        '''
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
        '''