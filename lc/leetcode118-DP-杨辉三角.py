class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[1], [1, 1]]

        def helper(list1):

            list2 = []
            list2.append(list1[0])
            for i in range(1, len(list1)):
                list2.append(list1[i] + list1[i - 1])
            list2.append(list1[-1])
            return list2

        for i in range(2, numRows):
            list2 = helper(res[-1])
            res.append(list2)

        return res