# 爬楼梯问题
def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    a = 1
    b = 2
    for i in range(3,n+1):
        a,b = b,a+b
    return b

print(climbStairs(10))

