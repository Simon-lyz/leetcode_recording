class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        tmp = 0
        if sum(gas) < sum(cost):
            return -1
        start = 0
        for i in range(n):
            tmp += gas[i] - cost[i]
            # 如果是负数，说明从start到i都不行，所以从i+1开始
            # 如果是正数，说明从start到i都可以，所以start不变
            if tmp < 0:
                tmp = 0
                start = i+1
        return start