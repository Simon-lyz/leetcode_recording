class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dict1 = {}
        for i in range(10):
            dict1[i] = i*i

        unreturndict = {}
        while True:
            list1 = []
            for i in range(len(str(n))):
                list1.append(n % 10)
                n //= 10

            for i in range(len(list1)):
                n += dict1[list1[i]]
            if n in unreturndict:
                return False
            else:
                unreturndict[n] = 1
            if n == 1:
                return True

        return False

