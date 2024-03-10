class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minp = 9999
        ans = 0
        n = len(prices)

        for i in range(n):
            minp = min(minp, prices[i])
            if minp < prices[i]:
                ans = max(ans,prices[i]-minp)

        return ans

