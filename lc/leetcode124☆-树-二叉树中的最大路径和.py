# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxsum = -9999
        def maxgain(root):
            if not root:
                return 0
            left = max(maxgain(root.left),0)
            right = max(maxgain(root.right),0)
            self.maxsum = max((left+right+root.val),self.maxsum)
            # 返回分支，这个分支是给父节点用的，要么返回左要么右
            return root.val+max(left,right)
        maxgain(root)
        return self.maxsum
