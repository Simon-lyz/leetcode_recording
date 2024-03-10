class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(list(set(nums)))
        cnt = 0
        tmp = 0
        for i in range(len(nums)-1):
            if nums[i] - nums[i+1] == -1:
                tmp += 1
            else:
                cnt = max(tmp,cnt)
                tmp = 0
                print(cnt)

        cnt = max(tmp,cnt)
        return cnt+1

