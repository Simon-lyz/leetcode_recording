class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [1] * n
        for i in range(1,n):
            left[i] = nums[i-1] * left[i-1]
        print(left)
        right = [1] * n
        for i in range(n-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]
        print(right)
        res = [0] * n
        for i in range(n):
            res[i] = left[i] * right[i]
        return res