class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = 0
        r = n-1
        minval = 9999
        while l <= r:
            mid = (l+r) // 2
            minval = min(nums[mid],minval)
            if nums[l] < nums[mid]:
                minval = min(nums[l],minval)
                l = mid+1
            if nums[mid] <= nums[r]:
                minval = min(nums[mid],minval)
                r = mid-1
            #print(l,r,mid)
        return minval
