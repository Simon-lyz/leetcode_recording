class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        
        a ^ a -> 0
        '''


        ans = 0
        for e in nums:
            ans ^= e

        return ans