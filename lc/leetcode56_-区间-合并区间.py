class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key = lambda x:x[0])
        res = [intervals[0]]
        for i in range(len(intervals)):
            left = intervals[i][0]
            right = intervals[i][1]
            if left <= res[-1][1]:
                res[-1][1] = max(res[-1][1],right)
            else:
                res.append([left, right])
        return res