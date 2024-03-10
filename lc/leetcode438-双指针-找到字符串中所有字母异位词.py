class Solution(object):
    def are_strings_equal(self,str1, str2):
        # 首先检查两个字符串的长度是否相同
        if len(str1) != len(str2):
            return False

        # 使用字典来统计每个字符在两个字符串中的出现次数
        char_count1 = {}
        char_count2 = {}

        # 统计第一个字符串中的字符出现次数
        for char in str1:
            if char in char_count1:
                char_count1[char] += 1
            else:
                char_count1[char] = 1

        # 统计第二个字符串中的字符出现次数
        for char in str2:
            if char in char_count2:
                char_count2[char] += 1
            else:
                char_count2[char] = 1

        # 检查两个字典是否相同（包含相同的字符和相同的出现次数）
        return char_count1 == char_count2


    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s)<len(p):
            return []

        res = []
        dict1 = [0]*26
        dict2 = [0]*26
        for i in range(len(p)):
            dict1[ord(s[i]) - 97] += 1
            dict2[ord(p[i]) - 97] += 1


        for i in range(len(s) - len(p) + 1):

            if dict1 == dict2:
                res.append(i)

            dict1[ord(s[i]) - 97] -= 1
            dict1[ord(s[i+len(p)]) - 97] += 1

        return res
