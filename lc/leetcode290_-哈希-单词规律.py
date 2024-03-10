class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split()
        if len(pattern) != len(s):
            return False
        else:
            return len(set(zip(pattern,s))) == len(set(pattern)) == len(set(s))

