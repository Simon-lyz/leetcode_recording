class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        print(m, n)
        cnt = 0
        i = 0
        j = 0
        top = m
        bottom = 0
        left = 0
        right = n
        res = []
        while cnt <= m * n:
            while left != right and i < right:
                res.append(matrix[bottom][i])
                cnt += 1
                i += 1
            bottom += 1
            i -= 1
            j += 1
            while bottom != top and j < top:
                res.append(matrix[j][right - 1])
                cnt += 1
                j += 1
            right -= 1
            j -= 1
            i -= 1
            while left != right and i >= left:
                res.append(matrix[top - 1][i])
                cnt += 1
                i -= 1
            top -= 1
            i += 1
            j -= 1
            while bottom != top and j >= bottom:
                res.append(matrix[j][left])
                cnt += 1
                j -= 1
            left += 1
            j += 1
            i += 1
            print(cnt)
            if cnt == m * n:
                break

        return res[:m * n]


