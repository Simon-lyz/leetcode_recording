class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        '''
        for i in range(m,m+n):
            nums1[i] = nums2[i]
            
        for i in range(m+n):
            for j in range(i,m+n-1):
                if nums1[j] > nums1[j+1]:
                    nums1[j],nums1[j+1]=nums1[j+1],nums1[j]
        '''

        p1 ,p2 = m-1,n-1
        tail = m+n-1

        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1





