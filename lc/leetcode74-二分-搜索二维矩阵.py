class Solution(object):
    def searchMatrix(self,matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        col = 0
        while True:
            try:
                if target >= matrix[col][0] and target <= matrix[col][-1]:
                    break
                elif target > matrix[col][-1]:
                    col += 1
                else:
                    return False
            except:
                return False

        lst = matrix[col]
        l = 0
        r = len(lst)
        while l < r:
            mid = (l+r) // 2
            if lst[mid] == target:
                return True
            if lst[mid] < target:
                l = mid+1
            else:
                r = mid
        return False

