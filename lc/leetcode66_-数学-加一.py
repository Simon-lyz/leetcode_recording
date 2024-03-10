class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        flag = 0
        digits[-1] += 1
        print(digits)
        for i in range(len(digits) - 1, -1, -1):

            if digits[i] + flag == 10:
                print(i)
                digits[i] = 0
                flag = 1
            else:
                digits[i] += flag
                flag = 0
        if flag == 1:
            return [1] + digits
        return digits