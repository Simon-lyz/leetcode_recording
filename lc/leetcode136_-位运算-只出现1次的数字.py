class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        collections.Counter(nums)
        for k,v in collections.Counter(nums).items():
            if v == 1:
                return k