class Solution(object):
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
                        s.append(int(float(a)//b))

        return s[-1]