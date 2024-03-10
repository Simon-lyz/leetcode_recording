class MinStack(object):
    def __init__(self):
        self.minstack = []
        self.s = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.s.append(val)
        self.minstack.append(val)
        self.minstack = sorted(self.minstack)

    def pop(self):
        """
        :rtype: None
        """
        val = self.s.pop()
        self.minstack.remove(val)

    def top(self):
        """
        :rtype: int
        """
        val = self.s.peek()
        #self.minstack.remove(val)
        return val

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()