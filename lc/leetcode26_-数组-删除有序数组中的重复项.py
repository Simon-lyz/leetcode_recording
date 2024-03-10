class Solution(object):
    def removeDuplicates(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow,fast = 1,1
        while fast < len(nums):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1

            fast += 1

        return slow

