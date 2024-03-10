class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))

'''

解题思路：
        1. 查找连续2个字符在字典中是否存在，存在加上对应数值，跳过刚用过的下一位，即i+= 2;
        2. 若不存在2个连续的字符，则将当前的字符对应的数值加上即可，更新i, i += 1
        
'''
'''
class Solution:
    def romanToInt(self, s):

        dict_num = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        res = 0
        i = 0

        while i < len(s):
            if s[i: i + 2] in dict_num:
                res += dict_num[s[i: i + 2]]
                i += 2
            else:
                res += dict_num[s[i]]
                i += 1
        return res
'''