# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
如图我们可以知道路径 [9, 4, 2, 5, 7, 8] 可以被看作以 222 为起点，从其左儿子向下遍历的路径 [2, 4, 9] 和从其右儿子向下遍历的路径 [2, 5, 7, 8] 拼接得到。

假设我们知道对于该节点的左儿子向下遍历经过最多的节点数 LLL （即以左儿子为根的子树的深度） 和其右儿子向下遍历经过最多的节点数 RRR （即以右儿子为根的子树的深度），那么以该节点为起点的路径经过节点数的最大值即为 L+R+1L+R+1L+R+1 。

我们记节点 node\textit{node}node 为起点的路径经过节点数的最大值为 dnoded_{\textit{node}}d
node
​
  ，那么二叉树的直径就是所有节点 dnoded_{\textit{node}}d
node
​
  的最大值减一。

最后的算法流程为：我们定义一个递归函数 depth(node) 计算 dnoded_{\textit{node}}d
node
​
  ，函数返回该节点为根的子树的深度。先递归调用左儿子和右儿子求得它们为根的子树的深度 LLL 和 RRR ，则该节点为根的子树的深度即为

max(L,R)+1max(L,R)+1max(L,R)+1

该节点的 dnoded_{\textit{node}}d
node
​
  值为

L+R+1L+R+1L+R+1

递归搜索每个节点并设一个全局变量 ansansans 记录 dnoded_\textit{node}d
node
​
  的最大值，最后返回 ans-1 即为树的直径
'''

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.height = 0

        def dfs(root):
            if not root:
                return 0
            L = dfs(root.left)
            R = dfs(root.right)
            self.height = max(self.height,L+R+1)
            return max(L,R)+1
        dfs(root)
        return self.height-1