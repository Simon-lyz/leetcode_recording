class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1] * len(nums)
        for i in range(1, len(left)):
            left[i] = left[i - 1] * nums[i - 1]
        print(left)

        right = [1] * len(nums)
        for i in range(len(left) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        print(right)
        res = [0] * len(nums)
        for i in range(len(left)):
            res[i] = left[i] * right[i]

        return res
