
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """

        def dfs(root,sumlist):
            if root is None:
                return 0
            sumlist = [num+root.val for num in sumlist]
            sumlist.append(root.val)

            count = sumlist.count(targetSum)
            return count + dfs(root.left,sumlist) + dfs(root.right,sumlist)

        return dfs(root,[])

