class Solution(object):
    def coinChange(self, coins, amount):
        # dp数组中存储了以目前的coins，完成amount最少需要几次
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            # 取最小的coin需要多少次cnt，依次递增
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1
