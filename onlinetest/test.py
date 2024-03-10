

while True:
    try:
        n_tasks = int(input())
        total_time = int(input())
        tasks = []

        for i in range(n_tasks):
            task = input().split()
            time = int(task[0])
            score = int(task[1])
            tasks.append((time,score))

        tasks = sorted(tasks,key = lambda x:(x[0],-x[1]))

        current_time = 0
        total_score = 0
        for sla,score in tasks:
            if current_time < sla and current_time < total_time:
                total_score += score
                current_time += 1

        print(total_score)

    except:
        break



'''
4
3
1 2
1 3
1 4
3 5
'''

