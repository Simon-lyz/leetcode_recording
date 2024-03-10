import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [i*i for i in range(1,int(n**0.5)+1)]
        def divisible(n,cnt):
            if cnt == 1: return n in nums
            for p in nums:
                if divisible(n-p,cnt - 1):
                    return True

            return False
        # 是几个完全平方的和？
        for cnt in range(1,n+1):
            if divisible(n,cnt):
                return cnt

        nums = [i * i for i in range(1, int(n ** 0.5) + 1)]
        f = [0] + [float('inf')] * n
        for num in nums:
            for j in range(num, n + 1):
                f[j] = min(f[j], f[j - num] + 1)

        print(f)
        return f[-1]




