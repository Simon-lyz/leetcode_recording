class Solution(object):
    def minSubArrayLen(self,target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < target:
            return 0
        i,j = 0,0
        n = len(nums)
        ans = n
        total = 0
        for e in nums:
            if e >= target:
                return 1

        '''
        # 时间复杂度超，答案正确
        while i < n:
            while j < n and sum(nums[i:j]) < target:
                j += 1
            if sum(nums[i:j]) >= target:
                ans = min(ans,j-i)
                print(ans,i,j)
            i += 1
        '''
        # 优化版本
        while j < n:
            total += nums[j]
            while total >= target:
                ans = min(ans, j - i + 1)
                total -= nums[i]
                i += 1
            j += 1
        return ans

print(Solution.minSubArrayLen(7,[2,3,1,2,4,3]))