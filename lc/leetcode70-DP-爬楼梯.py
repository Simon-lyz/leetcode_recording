class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 递归求解，但时间会超
        '''
            if n == 1: return 1
            if n == 2: return 2
            return self.climbStairs(n-1) + self.climbStairs(n-2)
        '''

        dp = []
        # 转移状态：dp[n+1] = dp[n] + dp[n-1]
        # 初始状态：dp[0] = 1，dp[1] = 1
        dp.append(1)
        dp.append(1)
        for _ in range(1,n):
            dp.append(dp[-1] + dp[-2])

        return dp[-1]