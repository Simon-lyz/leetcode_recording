import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(list)
        for s in strs:
            # key = sorted(s) : value = list
            ans[tuple(sorted(s))].append(s)

        return ans.values()