class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        slow = 0
        fast = 0
        ans = []
        while fast < len(nums):
            if fast == len(nums) - 1 or nums[fast] + 1 != nums[fast + 1]:
                if slow == fast:
                    ans.append(str(nums[slow]))
                else:
                    ans.append(str(nums[slow]) + "->" + str(nums[fast]))
                slow = fast + 1
            fast += 1
        return ans
