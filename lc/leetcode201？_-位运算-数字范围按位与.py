class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        while right > left:
            # right逐行减小。right-1 这个操作实际上是将right的最低位的1变成0
            #由于right逐渐减小，当它不再大于left时，它就是原始left和right的共同前缀。
            right &= right - 1
        return right