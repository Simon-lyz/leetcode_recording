# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        q = []
        if root: q.append(root)
        size = len(q)
        ordered = []
        while size:
            res.append(q[-1].val)
            for i in range(size):
                cur = q.pop(0)
                ordered.append(cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            size = len(q)

        return res
