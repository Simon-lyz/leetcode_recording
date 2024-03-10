# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def midorder(self, node):
        if node:
            self.midorder(node.left)
            self.mid.append(node.val)
            print(node.val)
            self.midorder(node.right)

    mid = []

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.mid = []
        self.midorder(root)
        print(self.mid)
        if len(self.mid) == 0:
            return True

        for i in range(1, len(self.mid)):
            if self.mid[i] <= self.mid[i - 1]:
                return False

        return True