class Solution(object):
    def largestRectangleArea(self,heights):

        """
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_res = 0
        for i in range(len(heights)):
            while len(stack) > 1 and heights[i] <= heights[stack[-1]]:
                max_res = max(max_res, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        for i in range(len(stack)-1):
            max_res = max(max_res, heights[stack.pop()]*(len(heights)-1-stack[-1]))
        return max_res

        """
        ans = 0
        stack = [-1] # 堆一个栈底
        for i in range(len(heights)):
            # 只要栈不为空，并且当前遍历的数据小于栈顶元素，则说明找到了右边界(i - 1)
            while len(stack) > 1 and heights[i] <= heights[stack[-1]]:
                h = heights[stack.pop()]
                l = (i - stack[-1] - 1)
                ans = max(ans, h * l)
                print(ans)
            # 栈为空或者当前遍历的数据大于等于栈顶数据，则入栈，不会执行上面的while循环
            # 保证了栈中的数据总是递增的 比如  0 1 2 2 3 4 4 5 6 ...
            stack.append(i)
        # 循环结束，要清理堆栈(递增的数据)。此时所有栈中继续存放的元素的右边界c都是结尾len(height)-1
        for i in range(len(stack)-1):
            h = heights[stack.pop()] # 高
            right = len(heights)-1
            left = stack[-1]
            l = right - left # 底
            ans = max(ans,  h * l)
        return ans


'''
# 单调栈的结构（存index）
list1 = [4,6,8,2,3]
stack = []
for i in range(len(list1)):
    while stack and list1[stack[-1]] > list1[i]: #先调整位置。
        stack.pop()
    stack.append(i)  #当前元素无论如何也要放进去，不同的只是需不需要pop来调整位置
    print(stack)


这个题的关键点在于：
以B点为高的矩形的最大宽度为， 从a到c， 其中a，c分别为B左边和右边第一个小于B的元素。
单调栈的特点在于：
当遇见大数的时候， 压入堆栈，等待之后处理。
当遇见小数c的时候，意味着大数b的右边界c已经确定了。
这时候开始pop， 而以被pop出来的值（b）为高度的矩形的左右边界需要被确定。
其右边界就是当前的小数。即为c。左边界是堆栈下一层的元素，因为下一层的元素一定比当前小。且是第一小的元素。这时候a也确定了。
则以被pop出来的数为高度的矩形是 (c - a - 1) * pop()， 这里pop() == b
'''