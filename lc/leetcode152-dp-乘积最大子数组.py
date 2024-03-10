class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        maxp = minp = ans = 0
        for i in range(n):
            if nums[i] < 0:
                maxp,minp = minp,maxp

            maxp = max(nums[i] , maxp * nums[i])
            minp = min(nums[i] , minp * nums[i])
            ans = max(maxp,ans)
        return ans