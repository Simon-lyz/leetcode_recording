class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return 0
        i = 0
        j = len(height) - 1
        maxa = 0
        while(i < j):
            maxa = max(maxa,(j - i) * min(height[i],height[j]))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return maxa