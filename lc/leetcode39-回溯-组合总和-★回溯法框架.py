class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        path = []
        candidates = sorted(candidates)
        def dfs(i, sum, path):
            if sum == target:
                ans.append(path[:])
                print(path[:])
                return
            for j in range(i, len(candidates)):
                if sum + candidates[j] > target:
                    return
                dfs(j, sum + candidates[j], path + [candidates[j]])

        dfs(0, 0, path)
        print(ans)
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
