# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        cur1 = head
        d = {}  # 用一个词典来存储复制的节点
        while cur1:
            d[cur1] = Node(cur1.val)
            cur1 = cur1.next

        cur1 = head

        while cur1:
            # p是原节点，d[cur1]是对应的新节点，cur1.next是原节点的下一个
            # d[cur1.next]是原节点下一个对应的新节点
            if cur1.next:
                d[cur1].next = d[cur1.next]
            if cur1.random:
                d[cur1].random = d[cur1.random]

            cur1 = cur1.next

        return d[head]
