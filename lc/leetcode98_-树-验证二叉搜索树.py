# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        lst = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            lst.append(root.val)
            dfs(root.right)

        dfs(root)
        for i in range(len(lst)-1):
            if lst[i+1]-lst[i]<= 0:
                return False
        return True
