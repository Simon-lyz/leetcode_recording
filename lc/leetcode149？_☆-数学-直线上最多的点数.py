class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # gcd(a,b)  求a和b的最大公约数
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        def get_slope(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            if dx == 0:
                return (0, 1)
            if dy == 0:
                return (1, 0)
            g = gcd(dx, dy)
            return (dx // g, dy // g)

        if len(points) <= 2:
            return len(points)

        res = 0
        for i in range(len(points)):
            slopes = {}
            same = 0
            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    same += 1
                    continue
                slope = get_slope(points[i], points[j])
                slopes[slope] = slopes.get(slope, 0) + 1
            print(slopes)
            if slopes:
                res = max(res, same + 1 + max(slopes.values()))
            else:
                res = max(res, same + 1)
        return res

'''
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 1:
            return 1
        def getkb(a,b):
            if a[0] == b[0]:
                return None,a[0]
            else:
                k = float((a[1]-b[1]))/(a[0]-b[0])
                b = a[1]-k*a[0]
                return k,b

        dic = {}
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                k,b = getkb(points[i],points[j])
                # print((points[i],points[j]),k,b)
                if k == None:
                    if (0,b) in dic:
                        dic[(0,b)] += 1
                    else:
                        dic[(0,b)] = 1
                else:
                    if (k,b) in dic:
                        dic[(k,b)] += 1
                    else:
                        dic[(k,b)] = 1
        # 4+3+2+1 = 10 input=10  return 4
        def help(i):
            j = 0
            while j <= i:
                j += 1
                i -= j
            return j
        print(dic)

        return help(max(dic.values()))+1 if dic else len(points)
'''