class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        d = collections.Counter(nums)
        return [item[0] for item in d.most_common(k)]
