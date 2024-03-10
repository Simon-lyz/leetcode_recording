
# list转string
lst = ["a","b","c"]
str1 = "".join(lst)
# list to numpy
import numpy as np
lst = [1,2,3]

# 测试流程？基于不同客户的数据，提升模型的一个准确性。文档检索，大模型其他，部门的正式员工
# 1. 测试数据
# 2. 测试函数
# 3. 测试样例
def get_max(lst):
    return max(lst)

def get_index(lst):
    return lst.index(max(lst))


'''
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
 

提示：

0 <= word1.length, word2.length <= 500
word1 和 word2 由小写英文字母组成


'''

def helper(word1,word2):
    m,n = len(word1),len(word2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    for i in range(1,m+1):
        for j in range(1,n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])


    for i in range(len(dp)):
        lst = []
        for j in range(len(dp[0])):
            lst.append(dp[i][j])
        print(lst)
    return dp[-1][-1]


word1 = "horse"
word2 = "ros"
print(helper(word1,word2))



