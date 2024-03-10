class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []

        def ispalid(s):
            return s == s[::-1]

        def backtrack(i, path):
            if i == len(s):
                ans.append(path[:])
                return

            # i 是起始位置，j是结束位置
            for j in range(i + 1, len(s) + 1):
                if ispalid(s[i:j]):
                    path.append(s[i:j])  # 加进去
                    backtrack(j, path)  # 递归，下一个起始位置是j，传进去path
                    path.pop()

        result = []
        backtrack(0, [])
        return result


'''
result = []
def backtrack(选择列表, 路径):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:

        # 做选择
        1. 路径.add(选择)
        2. (将该选择从选择列表移除)

        3. backtrack(选择列表, 路径) # 核心 递归调用之前【做选择】，调用之后【撤销选择】

        # 撤销选择
        4. 路径.remove(选择)
        5. (将该选择再加入选择列表)
'''