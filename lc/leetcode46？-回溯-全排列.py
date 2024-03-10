class Solution(object):
    def permute(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        path = [0] * n
        on_path = [False] * n
        ans = []
        def dfs(i):
            if i == n:
                ans.append(path[:])
                return
            for j,on in enumerate(on_path):
                if not on:
                    path[i] = nums[j]
                    on_path[j] = True # 选没有选的数
                    dfs(i+1)
                    on_path[j] = False # 恢复

        dfs(0)
        return ans


print(Solution.permute([1,2,3]))