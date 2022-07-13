import sys

sys.stdin = open('input.txt')

total_tc=int(input())

for tc in range (1, total_tc+1):
    N, M = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            for k in range(M):
                for l in range(M):
                    kill += table[i+k][j+l]


            if kill > max_kill:
                max_kill = kill

    print("#%d %d"%(tc, max_kill))