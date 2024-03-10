class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return max(nums)
        dp = nums[:1]
        dp.append(max(nums[:2])) # 第二晚肯定抢12两间最多的
        for i in range(2,len(nums)):
            dp.append(max(dp[i-1],dp[i-2]+nums[i]))

        print(dp)
        return dp[-1]