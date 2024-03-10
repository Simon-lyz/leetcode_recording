class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        rightmax = nums[0]
        for i in range(n):
            if i <= rightmax:
                break
            rightmax = max(i+nums[i],rightmax)
            if rightmax >= n-1:
                return True
        return False
