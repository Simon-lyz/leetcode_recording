import itertools
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 思路1：库函数
        res = []
        for i in range(len(nums)+1):
            '''
                内置库函数，获得nums中所有长度为i的组合
                当i=0时，没有组合（因为长度为0的组合只有一个空组合）。
                当i=1时，有3个长度为1的组合：[1], [2], [3]。
                当i=2时，有3个长度为2的组合：[1, 2], [1, 3], [2, 3]。
                当i=3时，有1个长度为3的组合：[1, 2, 3]。
            '''
            for tmp in itertools.combinations(nums, i):
                res.append(tmp)
            print(i,"",res)

        # 思路2：迭代求解，新来一个i，把i插进列表
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]

        # 思路3：递归-回溯算法
        res = []
        n = len(nums)
        def helper(i,tmp):
            print(i,"",tmp)
            res.append(tmp)
            for j in range(i,n):
                helper(j+1,tmp+nums[j])
        helper(0,[])
        return res