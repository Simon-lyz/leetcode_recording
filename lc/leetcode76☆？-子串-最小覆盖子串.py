import collections
class Solution(object):
    def minWindow(s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        needcnt = len(t)

        i = 0
        res = (0,999999)
        for index,c in enumerate(s):
            # 只找t里面的三个元素，若包含cnt就-1，其他元素放进去无所谓
            if need[c] > 0:
                needcnt -= 1
            need[c] -= 1

            if needcnt == 0: # step1：已经包含
                while True: # step2:移动左侧，寻找最小子串
                    c = s[i]
                    if need[c] == 0: # 找到t中缺的那个元素就退出
                        break
                    need[c] += 1
                    i += 1
                if index - i < res[1]-res[0]:
                    res = (i,index)

                need[s[i]] += 1 # i往前走一格，寻找新的满足条件的子串
                needcnt += 1
                i += 1
            print("need", need)
        return "" if res[1] > len(s) else s[res[0]:res[1]+1]

s = "ADOBECODEBANC"
t = "ABC"
print(Solution.minWindow(s,t))

