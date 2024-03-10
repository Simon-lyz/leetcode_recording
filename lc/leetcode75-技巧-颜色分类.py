class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]


        ptr = 0
        # 把所有0放在头部
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i],nums[ptr] == nums[ptr],nums[i]
                ptr += 1

        # ptr之前必定全是0了已经
        for i in range(len(nums)):
            if nums[i] == 1:
                nums[i],nums[ptr] == nums[ptr],nums[i]
                ptr += 1

        return nums