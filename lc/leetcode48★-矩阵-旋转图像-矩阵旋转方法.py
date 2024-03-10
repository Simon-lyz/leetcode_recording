class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        import numpy as np
        matrix[:] = list(zip(*matrix))[::-1]  # 旋转矩阵，逆时针90度 不加[::-1]是求转置
        matrix[:] = list(zip(*matrix))[::-1]  # 旋转矩阵，逆时针90度
        matrix[:] = list(zip(*matrix))[::-1]  # 旋转矩阵，逆时针90度
        return matrix