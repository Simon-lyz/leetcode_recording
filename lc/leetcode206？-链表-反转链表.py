
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        while current != None:
            next_node = current.next  # 保存下一个节点
            current.next = prev  # 反转当前节点的指针
            prev = current  # 移动前一个节点
            current = next_node  # 移动当前节点到下一个节点
        return prev