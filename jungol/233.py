
def dice(level, sum):
    if level == N:
        if sum == M:
            for d in dices:
                if d!= 0:
                    print(d, end=' ')
            print()
        return
    for i in range(1, 7):
        dices[level] = i
        dice(level+1, sum+i)
        dices[level]=0

dices = [0 for _ in range(10)]


N, M = map(int, input().split())


dice(0, 0)