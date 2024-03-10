def min_energy(bricks):
    n = len(bricks)
    if n > 8:
        return -1
    bricks.sort()
    bricks = bricks[::-1]
    #print(bricks)
    total = sum(bricks)
    for i in range(total//8,99999):
        cnt = [(brick-1)//i + 1 for brick in bricks]
        if sum(cnt) <= 8:
            return i
    return -1

while True:
    try:
        lst = list(map(int,input().split()))
        print(min_energy(lst))
    except:
        break
