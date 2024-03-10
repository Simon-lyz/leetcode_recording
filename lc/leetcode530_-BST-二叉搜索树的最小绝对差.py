# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        inorderlist = []
        def inorder(r):
            if r == None:
                return
            inorder(r.left)
            inorderlist.append(r.val)
            inorder(r.right)

        inorder(root)
        minval = 999999
        for i in range(len(inorderlist)-1):
            minval = min(minval, abs(inorderlist[i]-inorderlist[i+1]))
        return minval


