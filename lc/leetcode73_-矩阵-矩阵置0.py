class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if len(matrix)==0:
            return matrix
        if len(matrix[0])==0:
            return matrix

        rows = [False]*len(matrix)
        cols = [False]*len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    rows[i]=True
                    cols[j]=True
        print(rows)
        print(cols)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if rows[i] or cols[j]:
                    matrix[i][j]=0

