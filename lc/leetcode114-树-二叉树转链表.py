# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.preorder = []
        def help(root):
            if root:
                self.preorder.append(root.val)
                help(root.left)
                help(root.right)
        help(root)
        print(self.preorder)
        node = root
        for i in range(1,len(self.preorder)):
            node.right = TreeNode(self.preorder[i])
            node.left = None
            node = node.right

