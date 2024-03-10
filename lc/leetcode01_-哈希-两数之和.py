class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}
        for i in range(len(nums)):
            dict1[target - nums[i]] = i

        for i in range(nums):
            if nums[i] in dict1.keys() and dict1[nums[i]] > i:
                return [i,dict1[i]]
        return [-1,-1]