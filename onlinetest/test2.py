# 现有N个任务需要处理，同一时间只能处理一个任务，处理每个任务所需要的时间固定为1。
# 每个任务都有最晚处理时间限制和积分值，在最晚处理时间点之前处理完成任务才可获得对应的积分奖励。
# 可用于处理任务的时间有限，请问在有限的时间内，可获得的最多积分。

# 输入描述
# 第一行为一个数N，表示有N个任务，1<=N<=100
# 第二行为一个数T，表示可用于处理任务的时间。1<=T<=100
# 接下来N行，每行两个空格分隔的整数(SLA和V)，SLA表示任务的最晚处理时间，V表示任务对应的积分。1<=SLA<=100, 0<=V<=100000

# 输出描述
# 可获得的最多积分
dic = {}
n_tasks = 5
total_time = 3
sla_list = [1,1,1,3,3]
scores = [2,3,4,5,6]

def max_score(n_tasks,total_time,sla_list,scores):
    #tasks = sorted([(sla_list[i],scores[i]) for i in range(n_tasks)],key = lambda x:(x[0],-x[1]))
    dp = [[0] * (total_time+1) for _ in range(n_tasks+1)]
    #print(tasks)

    for i in range(1,n_tasks+1):
        for j in range(1,total_time+1):
            # 如果当前任务的sla大于当前时间，那么可以做
            dp[i][j] = dp[i-1][j]
            #print(sla_list[i - 1],"i=",i,"j=", j, ",", dp[i])
            if sla_list[i-1] < j:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = max(dp[i-1][j-1] + scores[i-1], dp[i][j])

    for i in range(n_tasks+1):
        print(dp[i])
    return dp[n_tasks][total_time]

print(max_score(n_tasks,total_time,sla_list,scores))

'''
4
3
1 2
1 3
1 4
3 5
'''






