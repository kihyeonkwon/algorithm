import sys
sys.stdin = open('5247.txt')

TC = int(input())


for tc in range(1, TC+1):
    N, M = map(int, input().split())
    count = 0
    Q = [[N, count]]
    while Q:
        value = Q.pop(0)
        if value[0] > 1000000:
            continue
        if value[0] == M:
            print("#%d"%(tc), value[1])
            break

        else:
            Q.append([value[0] + 1, value[1] + 1])
            Q.append([value[0] * 2, value[1] + 1])
            Q.append([value[0] - 1, value[1] + 1])
            Q.append([value[0] - 10, value[1] + 1])









