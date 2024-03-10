# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        stacks = []
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        cnt = 0
        while cur:
            cnt += 1
            cur = cur.next
        for _ in range(0,cnt,k):
            stack = []
            if cnt - _ < k:
                for i in range(cnt-_):
                    stack.append(head)
                    head = head.next
            else:
                for i in range(k):
                    stack.append(head)
                    head = head.next
        cur = dummy
        for i in range(len(stacks)):
            if i == len(stacks) - 1:
                cur.next = stacks[i].pop(0)
            else:
                for _ in stacks[i]:
                    cur.next = stacks[0].pop(-1)
                    cur = cur.next
        return dummy.next





