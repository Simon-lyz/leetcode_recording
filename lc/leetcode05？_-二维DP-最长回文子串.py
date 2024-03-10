class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 外层循环是长度
        for l in range(n):
            # 内层循环是起始位置
            for i in range(n):
                j = i + l
                if j >= n:
                    break
                if l == 0: # 自己一定是回文子串
                    dp[i][j] = True
                elif l == 1: # 两个相邻的字符相等的话也是
                    dp[i][j] = (s[i] == s[j])
                else: # 三个以上的字符，首尾相等且去掉首尾的子串也是回文子串
                    dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans
