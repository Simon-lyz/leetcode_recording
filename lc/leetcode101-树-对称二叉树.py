# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def isSym(r1, r2):
            if not r1 and not r2:
                return True
            elif r1 == None or r2 == None or r1.val != r2.val:
                return False
            else:
                return isSym(r1.left, r2.right) and isSym(r1.right, r2.left)

        return isSym(root.left, root.right)

