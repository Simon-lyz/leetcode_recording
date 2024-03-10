class Solution(object):
    def groupAnagrams(self, strs):
        dict1 = {}
        for s in strs:
            sorted_s = str("".join(sorted(s)))
            if sorted_s not in dict1:
                dict1[sorted_s] = [s]
            else:    
                dict1[sorted_s].append(s)
        return list(dict1.values())