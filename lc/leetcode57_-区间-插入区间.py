class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        # 1. 将newInterval插入到intervals中
        intervals.append(newInterval)
        # 2. 对intervals按照第一个元素进行排序
        intervals = sorted(intervals, key=lambda x: x[0])
        # 3. 合并区间
        res = [intervals[0]]
        for i in range(len(intervals)):
            left = intervals[i][0]
            right = intervals[i][1]
            if left <= res[-1][1]:
                res[-1][1] = max(res[-1][1], right)
            else:
                res.append([left, right])
        return res