class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        cnt = dict(collections.Counter(nums))
        slow,fast = 1,1
        if nums[0] == nums[1]:
            b = True
        else:
            b = False
        while fast < len(nums):
            if nums[fast] == nums[fast-1] and not b:
                nums[slow] = nums[fast]
                b = True
                slow += 1
            elif nums[fast] == nums[fast-1] and b:
                continue
            else:
                nums[slow] = nums[fast]
                b = False
                slow += 1
            fast += 1
            return slow











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

