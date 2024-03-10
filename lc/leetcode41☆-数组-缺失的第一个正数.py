class Solution(object):
    def firstMissingPositive(self, nums):
        dict1 = {}
        for e in nums:
            dict1[e] = 1
        for i in range(1,len(nums)+1):
            if i not in dict1:
                return i
        return max(nums) + 1

