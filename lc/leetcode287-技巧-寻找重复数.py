class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s_nums = sorted(nums)
        for i in range(1,len(nums)):
            if s_nums[i] == s_nums[i-1]:
                return s_nums[i]
        '''
        def bs(arr,left,right):
            if right > left:
                mid = (left+right) // 2
                if arr[mid] == arr[mid-1]:
                    ans = mid
                    return
                elif mid == arr[mid]:
                    bs(arr,mid+1,right)
                else:
                    bs(arr,left,mid-1)
            else:
                return
        bs(s_nums,0,len(nums)-1)
        return ans
        '''