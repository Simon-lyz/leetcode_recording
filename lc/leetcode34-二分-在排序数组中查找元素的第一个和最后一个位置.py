class Solution(object):
    def searchRange( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        l = 0
        r = len(nums)
        '''
        while l < r:
            mid = (l+r) // 2
            if nums[mid] == target:
                i = mid
                j = mid
                if nums[0] == target:
                    i = 0
                else:
                    while nums[i] == nums[mid]:
                        i -= 1
                    i += 1
                if nums[len(nums) - 1] == target:
                    j = len(nums) - 1
                else:
                    while nums[j] == nums[mid]:
                        j += 1
                    j -= 1
                return [i,j]
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid
        return [-1,-1]
        '''

        # 优化版本
        # 找first
        l = 0
        r = len(nums) - 1
        first = -1
        last = -1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                first = mid
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        # 找last
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                last = mid
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return [first,last]

nums = [5, 7, 7, 8, 8, 10]
target = 8
print(Solution.searchRange(nums,target))