class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0, len(nums)
        while l<r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid+1
            else:
                if nums[mid] <= target <= nums[r-1]:
                    l = mid+1
                else:
                    r = mid

        return -1

