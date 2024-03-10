class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''
        1. 先找出第一个逆序k，满足nums[k]<nums[k+1]，如果不存在，就翻转整个数组；
        2. 再找出另一个最大索引 l 满足 nums[l] > nums[k]；
        3. 交换 nums[l] 和 nums[k]；
        4. 最后翻转 nums[k+1:]。    
        '''
        n = len(nums)
        k = -1
        for i in range(n-2,-1,-1):
            if nums[i+1] > nums[i]:
                k = i
                break
        l = -1
        for i in range(n-1,-1,-1):
            if nums[i] > nums[k]:
                l = i
                break
        def reverse(nums,i,j):
            while i < j:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1

        if k == -1:
            return reverse(nums,0,n-1)
        else:
            nums[l],nums[k] = nums[k],nums[l]
            return reverse(nums,k+1,n-1)
