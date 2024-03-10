class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        l = 0
        r = n
        while l < r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            # 判断有序
            if nums[l] < nums[mid]:
                # 左边有序且在范围内
                if nums[l] <= target < nums[mid]:
                    r = mid
                # 否则去右边找
                else:
                    l = mid + 1
            else:
                # 右边有序，且在右边范围内
                if nums[mid] <= target <= nums[n-1]:
                    l = mid+1
                else:
                    r = mid

        return -1