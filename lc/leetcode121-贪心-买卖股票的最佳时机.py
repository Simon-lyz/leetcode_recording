class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int.

        """
        low = 9999
        res = 0
        for i in range(len(prices)):
            low = min(low,prices[i])
            res = max(res,prices[i]-low)
        return res


