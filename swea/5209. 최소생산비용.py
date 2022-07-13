import sys
sys.stdin = open('5209.txt')


def production(n, sum):
    global min_sum
    if sum > min_sum:
        return 1

    if n == N:
        min_sum = min(sum, min_sum)
        return 1

    for i in range(N):
        if built[i]==False:
            built[i] = True
            production(n+1, sum +cost[n][i])
            built[i] = False



TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range (N)]
    built = [False for _ in range(N)]
    min_sum = 0xfffffff
    production(0, 0)
    print('#%d'%(tc), min_sum)