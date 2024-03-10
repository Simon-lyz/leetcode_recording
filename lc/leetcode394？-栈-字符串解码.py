import re

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for c in s:
            if c == "]":
                repeat = ""
                strs = ""
                while stack[-1] != "[":
                    strs = stack.pop() + strs
                # 遇到'[' 退出
                stack.pop()
                while stack and stack[-1].isdigit():
                    repeat = stack.pop() + repeat
                stack.append(int(repeat) * strs)
            stack.append(c)
            continue
        print(stack)
        return "".join(stack)


