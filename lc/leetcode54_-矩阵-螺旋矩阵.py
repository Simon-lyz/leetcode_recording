class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        row = len(matrix)
        col = len(matrix[0])

        left = 0
        right = col - 1
        top = 0
        bottom = row - 1
        ans = []
        while(left<= right and top <= bottom):
            for i in range(left,right+1):
                ans.append(matrix[top][i])

            top += 1
            for j in range(top,bottom+1):
                ans.append(matrix[j][right])

            right -= 1

            for i in range(right,left-1,-1):
                ans.append(matrix[bottom][i])
            bottom -= 1
            for j in range(bottom,top-1,-1):
                ans.append(matrix[j][left])
            left += 1

        return ans[:row*col]


