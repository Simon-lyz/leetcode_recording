class Solution(object):
    def removeElement(self,nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        while val in nums:
            nums.remove(val)
        return len(nums)


Solution.removeElement([0,1,2,2,3,0,4,2],2)