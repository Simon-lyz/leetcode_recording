class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # string.isalnum() 查看string中是否只包含字符串和数字
        # sgood = "".join(ch.lower() for ch in s if ch.isalnum())

        return s == s[::-1]
