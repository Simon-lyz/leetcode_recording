class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 最长有效括号，输入含有括号的字符串，输入最长有效括号的长度
        # 1. 暴力法，遍历所有子串，判断是否是有效括号，如果是，记录最大长度
        # 2. 动态规划
        # dp[i]表示以i结尾的最长有效括号的长度
        # 如果s[i] == '('，dp[i] = 0
        # 如果s[i] == ')'，如果s[i-1] == '('，dp[i] = dp[i-2] + 2
        # 如果s[i] == ')'，如果s[i-1] == ')'，如果s[i-dp[i-1]-1] == '('，dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
        if len(s) == 0:
            return 0

        dp = [0] * len(s)
        maxans = 0


        for i in range(len(s)):
            if s[i] == "(":
                dp[i] = 0
            if i>0 and s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2
                    maxans = max(maxans,dp[i])
                elif i - dp[i - 1] - 1 >= 0 and s[i-1] == ")":
                    if s[i-1-dp[i-1]] == "(":
                        # 分别是 dp[i-1]+2 当前括号长度 + 原先累计的长度
                        dp[i] = dp[i-1]+2+dp[i-1-dp[i-1]-1]
                        maxans = max(maxans, dp[i])

        return maxans





