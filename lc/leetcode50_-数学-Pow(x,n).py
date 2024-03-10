class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def help(n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n%2 == 0:
                return help(n//2)*help(n//2)
            else:
                return help(n//2)*help(n//2)*x

        return help(n) if n >= 0 else 1/help(-n)