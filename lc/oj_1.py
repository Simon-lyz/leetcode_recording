#1 2 3
#4 5
#0 0 0 0 0

#6
#9
#0

while True:
    try:
        lst = input().split()
        print(sum(list(map(int, lst))))
    except:
        break

