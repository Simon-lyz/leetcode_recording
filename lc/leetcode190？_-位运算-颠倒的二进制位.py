class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # n(int,10)转化为 二进制 bin(n)[2:]  补全到32位,结果是str，所以可以直接反转
        print((bin(n)[2:].zfill(32))) # 可以直接翻转


        return int(bin(n)[2:].zfill(32)[::-1],2)


