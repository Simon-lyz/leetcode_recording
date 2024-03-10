class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        #至少h篇论文被引用的次数>=h
        citations = sorted(citations,reverse=True)
        maxh = 0
        for i in range(len(citations)):
            maxh = max(min(citations[i],i+1),maxh)

        return maxh
