class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        s = []
        for p in path.split("/"):
            if p == "..":
                if s:
                    s.pop()
            elif p and p != ".":
                s.append(p)

        return "/" + "/".join(s)

