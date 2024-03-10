class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0, len(nums)
        while l<r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid

        return l

        '''
            思路:
            1. 先确定左右开闭 -> 左闭右开[left,right)
            2. 根据开闭确定数组长度 -> [0, len(nums)-1] // [0, len(nums))
            3. 循环结束条件 左闭右开 -> left<right,
            4. 中间值 mid = l + (r-l)//2 比 mid = (l+r)//2写法要好,防止溢出
            5★. 比较关系: 这里是难点,要根据题目来写.
            简单来说就是如果是<, 那么当nums[mid]达到是比target小的数中的最大的数的时候, 通过if条件进入, left的值为mid+1后的值必然是大于等于target的值, 这时候可能取到和target相等的位置.
            但是当换成≤时, 当nums[mid] == target时, 仍然会进入if条件, left的值为mid+1后的值必然是大于target的值, 这时候就不可能取到和target相等的位置. 就会收敛到第一个大于target的位置.

            6. 区间变化: 左闭右开 -> left = mid+1  right = mid, (实际是mid-1)
            7. 结束while时, l = r
        '''

'''

左闭右闭的写法
class Solution {
    public static  int searchInsert(int[] nums, int target) {
        int low = 0;
        int high = nums.length-1;
        int mid = 0;
        while(low <= high){
            mid = (low + high) /2;
            if(target == nums[mid]) return mid;
            if(target > nums[mid]) low = mid+1;
            else high = mid -1;
        }
        return low;
    }
}

'''


'''

    /**
     * 范围查询规律
     * 初始化:
     *   int left = 0;
     *   int right = nums.length - 1;
     * 循环条件
     *   left <= right
     * 右边取值
     *   right = mid - 1
     * 左边取值
     *   left = mid + 1
     * 查询条件
     *   >= target值, 则 nums[mid] >= target时, 都减right = mid - 1
     *   >  target值, 则 nums[mid] >  target时, 都减right = mid - 1
     *   <= target值, 则 nums[mid] <= target时, 都加left = mid + 1
     *   <  target值, 则 nums[mid] <  target时, 都加left = mid + 1
     * 结果
     *   求大于(含等于), 返回left
     *   求小于(含等于), 返回right
     * 核心思想: 要找某个值, 则查找时遇到该值时, 当前指针(例如right指针)要错过它, 让另外一个指针(left指针)跨过他(体现在left <= right中的=号), 则找到了
     */

'''