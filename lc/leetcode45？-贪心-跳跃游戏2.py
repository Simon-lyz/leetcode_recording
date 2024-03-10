class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxpos , end , step = 0,0,0
        for i in range(n-1):
            if maxpos >= i:
                maxpos = max(maxpos,i+nums[i])
                if i == end:
                    end = maxpos
                    step += 1
                    print(end)

        return step