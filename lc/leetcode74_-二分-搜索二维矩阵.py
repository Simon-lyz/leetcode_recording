class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m,n = len(matrix), len(matrix[0])
        l,r = 0, m*n
        while l<r:
            mid = (l+r)//2
            if matrix[mid//n][mid%n] < target:
                l = mid+1
            else:
                r = mid
        return l<m*n and matrix[l//n][l%n] == target
