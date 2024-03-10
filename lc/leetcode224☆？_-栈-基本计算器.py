class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 计算器 三步：
        # 1. 去掉空格和负数
        # 2. 中缀表达式转后缀表达式
        # 3. 计算后缀表达式
        s = s.replace(" ","")
        postfix = self.infix2postfix(s)
        return self.evalRPN(postfix)
    def infix2postfix(self, s):
        stack = []
        postfix = []
        for c in s:
            if c.isdigit():
                postfix.append(c)
            elif c in "+-":
                while stack and stack[-1] in "+-*/":
                    postfix.append(stack.pop())
                stack.append(c)
            elif c in "*/":
                while stack and stack[-1] in "*/":
                    postfix.append(stack.pop())
                stack.append(c)
            elif c == "(":
                stack.append(c)
            elif c == ")":
                while stack and stack[-1] != "(":
                    postfix.append(stack.pop())
                stack.pop()
        while stack:
            postfix.append(stack.pop())
        return postfix


    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []
        for token in tokens:
            if token not in "+-*/":
                s.append(int(token))
            if s:
                if token in "+-*/":
                    b = s.pop()
                    a = s.pop()
                    if token == "+":
                        s.append(a + b)
                    elif token == "-":
                        s.append(a - b)
                    elif token == "*":
                        s.append(a * b)
                    else:
                        s.append(int(float(a) // b))

        return s[-1]
