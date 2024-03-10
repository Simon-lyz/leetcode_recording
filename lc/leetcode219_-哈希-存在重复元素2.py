class Solution(object):
    #def containsNearbyDuplicate(self, nums, k):
    def solution(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] in dict1 and i - dict1[nums[i]] <= k:
                return True
            dict1[nums[i]] = i
        return False