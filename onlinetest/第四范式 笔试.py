'''
题目描述：
牛牛对个城市的旅游情况进行了规划。
已知每个城市有两种属性x_i和y_i，其中x_i表示去第号城市的花费，y_i表示在第i号城市游玩后会得到的开心值。
现在牛牛希望从中挑选出一些城市去游玩，但挑选出的城市必须满足任意两个城市之间花费的绝对值小于k。
他想请你帮他计算出在满足上述条件下能得到的最大开心值是多少？

输入描述：
第一行输入两个正整数n和k。
接下来n行.每行输入两个整数x_i和y_i，分别表示每个城市的两种属性。
1<= n <=10^5

输出描述：
输出一个整数，表示能得到的最大开心值。
'''
'''
def helper(n, k, cities):
    cities = sorted(cities, key=lambda x: x[0])
    dp = [0] * n
    for i in range(n):
        for j in range(i):
            if abs(cities[i][0] - cities[j][0]) < k:
                dp[i] = max(dp[i], dp[j])
        dp[i] += cities[i][1]
        print(dp[i])


    return max(dp)


        
'''



