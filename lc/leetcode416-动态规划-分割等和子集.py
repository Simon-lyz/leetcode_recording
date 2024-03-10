class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        # 分割等和子集，输入一个list，输出true/false
        # 本质是一个背包问题，背包容量为target，物品重量为nums[i]
        # 本题要求背包恰好装满，所以dp数组初始化为False

        dp = [False] * (target + 1)
        # base case
        dp[0] = True


        # 遍历物品
        for i in range(len(nums)):
            for j in range(target,nums[i]-1,-1):
                dp[j] = dp[j] or dp[j-nums[i]]
        print(dp)
        return dp[target]