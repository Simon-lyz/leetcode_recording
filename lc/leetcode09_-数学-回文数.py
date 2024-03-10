class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        l = []
        for i in str(x):
            l.append(i)

        return "".join(l[::-1]) == str(x)