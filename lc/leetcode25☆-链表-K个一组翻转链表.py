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

        dummyhead = ListNode(0)
        dum = dummyhead
        stacks = []
        cur = head
        cnt = 0
        while cur:
            cur = cur.next
            cnt += 1
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
            stacks.append(stack)
        for i in range(len(stacks)):
            stack = stacks[i]
            if len(stack) == k:
                for j in range(k):
                    node = stack.pop(-1)
                    dum.next = ListNode(node.val)
                    dum = dum.next
            else:
                for j in range(len(stack)):
                    node = stack.pop(0)
                    dum.next = ListNode(node.val)
                    dum = dum.next
        return dummyhead.next


'''

翻转链表

class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        
        return hair.next

作者：力扣官方题解
链接：https://leetcode.cn/problems/reverse-nodes-in-k-group/solutions/248591/k-ge-yi-zu-fan-zhuan-lian-biao-by-leetcode-solutio/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''