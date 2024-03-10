class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1 = {}
        start = 0
        maxlen = 0
        for i in range(len(s)):
            if s[i] in dict1 and dict1[s[i]] >= start:
                start = dict1[s[i]] + 1
            dict1[s[i]] = i
            maxlen = max(maxlen,i-start+1)

        return maxlen



