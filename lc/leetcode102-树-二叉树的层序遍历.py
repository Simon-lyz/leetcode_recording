# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = [root]

        res = []
        while q:
            size = len(q)
            tmplist = []
            print("size", size)
            for _ in range(size):
                cur = q.pop(0)
                tmplist.append(cur.val)
                if cur.left:  q.append(cur.left)
                if cur.right:  q.append(cur.right)

            res.append(tmplist)
        return res
