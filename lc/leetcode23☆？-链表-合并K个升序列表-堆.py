# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return

        # 优化
        import heapq

        queue = []
        dummy = ListNode(0)
        p = dummy

        for i in range(len(lists)):
            head = lists[i]
            # 把每个list都扔到堆里
            while head:
                heapq.heappush(queue, (head.val, head))
                head = head.next

        while queue:
            _, p.next = heapq.heappop(queue)  # 最小的那个丢出来
            p = p.next
        p.next = None
        return dummy.next