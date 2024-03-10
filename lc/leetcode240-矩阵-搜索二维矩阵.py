class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        i, j = 0, len(matrix[0]) - 1

        while True:
            if i >= len(matrix) or j < 0:
                break
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                j -= 1
            else:
                i += 1

        return False

        # for i in range(len(matrix)):
        #     if target in matrix[i]:
        #         return True
        # return False

