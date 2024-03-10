class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        import collections
        if len(magazine) < ransomNote:
            return False
        print(collections.Counter(ransomNote) - collections.Counter(magazine))
        # 如果由magazine组成，那么magazine里面字符范围一定更广，可以包含ransomNote
        return not collections.Counter(ransomNote) - collections.Counter(magazine)