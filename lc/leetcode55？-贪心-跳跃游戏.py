class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)
        if n == 1:
            return True
        rightmax = 0
        for i in range(n - 1):
            if i <= rightmax:
                rightmax = max(rightmax, i + nums[i])

                if rightmax >= n - 1:
                    return True

        return False