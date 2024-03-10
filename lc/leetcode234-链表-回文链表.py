# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        cur = head
        cnt = 0
        while cur != None:
            cnt += 1
            cur = cur.next
        print(cnt)
        cur = head
        # while cur != None and cur not in stack:
        #     stack.append(cur)
        #     cur = cur.next
        i = 0
        if cnt % 2 == 0:
            for i in range(cnt // 2):
                stack.append(cur)
                cur = cur.next
            print(len(stack))
            while cur != None:
                if stack.pop(-1).val != cur.val:
                    return False
                cur = cur.next
            if (len(stack) == 0):
                return True
            else:
                return False
        else:
            for i in range(cnt // 2 + 1):
                stack.append(cur)
                cur = cur.next

            print(len(stack))
            while cur != None:
                if stack.pop(-2).val != cur.val:
                    return False
                cur = cur.next
            if (len(stack) == 1):
                return True
            else:
                return False