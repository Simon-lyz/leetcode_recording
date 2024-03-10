class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        rightmax = 0
        steps = 0
        end = 0
        for i in range(n-1):
            if i + nums[i] >= n-1:
                return steps+1
            if rightmax >= i:
                rightmax = max(rightmax,i+nums[i])
                if i == end:
                    steps += 1
                    end = rightmax

        return steps