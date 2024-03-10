s = "aabaab!ba"



def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    maxn = 0
    tmps = ""
    for i in range(len(s)):
        if tmps.find(s[i]) == -1:
            tmps += s[i]
            maxn = max(maxn,len(tmps))
        else:
            tmps = tmps[tmps.rfind(s[i])+1:]+s[i]
            print("lala",tmps)
        print(tmps)
        print(maxn)
        print("*"*20)
    return maxn

lengthOfLongestSubstring(s)