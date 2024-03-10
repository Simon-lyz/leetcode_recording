# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(pl,pr,il,ir):
            if pl>pr: return None
            rootval = preorder[pl]
            root = TreeNode(preorder[pl])

            # in_rootidx = -1
            # for i in range(len(inorder)):
            #     if inorder[i] == rootval:
            #         in_rootidx == i
            #         print(in_rootidx)
            in_rootidx = index[preorder[pl]]

            leftsize = in_rootidx - il

            root.left = helper(pl+1,pl+leftsize,il,in_rootidx-1)
            root.right = helper(pl+leftsize+1,pr,in_rootidx+1,ir)
            return root

        index = {element: i for i, element in enumerate(inorder)}
        return helper(0,len(preorder)-1,0,len(preorder)-1)

