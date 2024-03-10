#
# 给你一个正整数数组 values，其中 values[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的 距离 为 j - i。
# 一对景点（i < j）组成的观光组合的得分为 values[i] + values[j] + i - j ，也就是景点的评分之和 减去 它们两者之间的距离。
# 返回一对观光景点能取得的最高分。

def maxScoreSightseeingPair(values):
    # 初始化最大得分和迄今为止的最大values[i] + i
    max_score = 0
    max_i = values[0]  # 因为i从0开始，所以初始值是values[0] + 0

    # 从第二个景点开始遍历
    for j in range(1, len(values)):
        # 更新最大得分
        max_score = max(max_score, max_i + values[j] - j)
        # 更新迄今为止的最大values[i] + i
        max_i = max(max_i, values[j] + j)

    return max_score

def helper(values):
    max_score = 0
    max_i = values[0] + 0 #因为i从0开始，所以初始值是values[0] + 0

    for j in range(1, len(values)):
        # max_i + values[j] - j 表示当前景点的得分
        # value[i] + i
        max_score = max(max_score, max_i + values[j] - j)

        max_i = max(max_i, values[j] + j)
        print(max_i)

    return max_score

values = [6,1,9,2,7]
print(helper(values))  # 11