# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.mid = []

        def midorder(root):
            if root:
                midorder(root.left)
                self.mid.append(root.val)
                midorder(root.right)

        midorder(root)
        print(self.mid)
        return self.mid[k - 1]
