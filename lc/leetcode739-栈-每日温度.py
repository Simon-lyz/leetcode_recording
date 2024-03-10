class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        ans = [0] * n
        '''
            暴力解法 时间复杂度O n*m
        '''

        for i in range(len(temperatures)-1):
            for j in range(i,n):
                if temperatures[j] > temperatures[i]:
                    ans[i] = j-i
                    break
        print(ans)
        return ans

        '''
            单调栈 时间复杂度O n
        '''

        stack = []
        for i in range(n):
            temperature = temperatures[i]
            while stack and temperature > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans
