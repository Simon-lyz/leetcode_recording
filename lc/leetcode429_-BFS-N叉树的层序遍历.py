class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        ans = []
        while queue:
            ans.append([node.val for node in queue])
            queue = [child for node in queue for child in node.children if child]  # 更新queue为下一层的所有子节点
        return ans
