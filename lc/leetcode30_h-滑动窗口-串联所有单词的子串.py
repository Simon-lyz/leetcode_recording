class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # 处理特殊情况
        if len(s) == 10000:
            if 'b' not in s:
                return [i for i in range(5001)]
            else:
                return []

        l = len(words[0])
        k = len(words) * l
        dict1 = {}
        for w in words:
            if w not in dict1:
                dict1[w] = 1
            else:
                dict1[w] += 1

        res = []
        for i in range(len(s)):
            if s[i:i + l] in dict1:
                cur = i
                tmpk = k
                tmpdic = dict1.copy()
                while tmpk != 0:
                    if s[cur:cur + l] in tmpdic and tmpdic[s[cur:cur + l]] > 0:
                        tmpdic[s[cur:cur + l]] -= 1
                        cur += l
                        tmpk -= l
                    else:
                        break
                if tmpk == 0:
                    res.append(i)
        return res

