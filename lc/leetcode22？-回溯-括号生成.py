class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(tmp,l,r):
            if 2*n == len(tmp):
                ans.append(tmp)
                return
            # 先把左括号消耗完
            if l > 0 :
                backtrack(tmp+"(",l-1,r)
            # 右比左多则可以消耗右
            if r > l:
                backtrack(tmp+")",l,r-1)


        backtrack('',n,n)
        return ans
'''     
result = []
def backtrack(选择列表, 路径):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        # 做选择
        路径.add(选择)
        将该选择从选择列表移除

        backtrack(选择列表, 路径) # 核心 递归调用之前【做选择】，调用之后【撤销选择】

        # 撤销选择
        路径.remove(选择)

        将该选择再加入选择列表
'''