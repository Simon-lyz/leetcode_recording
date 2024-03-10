class Solution(object):
    def findKthLargest(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
            快速排序
        '''
        def partition(nums,left,right):
            pivot = nums[left]
            i,j = left,right
            while(i<j):
                while i<j and nums[j] > pivot:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] <= pivot:
                    i += 1
                nums[j] = nums[i]
            nums[i] = pivot
            return i

        def quicksort(nums,left,right):
            if left<right:
                index = partition(nums,left,right)
                quicksort(nums,left,index-1)
                quicksort(nums,index+1,right)

        ''' 
            arr = [1,3,2,4,0]
            quicksort(arr,0,len(arr)-1
        '''
        '''
            快速选择，选择第k个位置
        '''

        # 需要注意这边只会排序前k个位置
        def topk_split(nums,k,left,right):
            if left<right:
                index = partition(nums,left,right)
                if index == k:
                    return
                elif index < k:
                    topk_split(nums,k,index+1,right)
                else:
                    topk_split(nums,k,left,index-1)

        # # 获取前k小的数
        # topk_split(nums,k,0,len(nums)-1)
        # return nums[:k]
        #
        # # 获取第k小的数
        # topk_split(nums, k, 0, len(nums) - 1)
        # return nums[k]

        # 获得第K大的数
        topk_split(nums, len(nums)-k, 0, len(nums) - 1)
        return nums[len(nums)-k]


nums = [3,2,1,5,6,4]
k = 2
print(Solution.findKthLargest(nums,k))