import sys

sys.stdin = open('input.txt')

total_tc = int(input())

for tc in range (1, total_tc+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    print('#%d'%(tc))
    for i in range(N):
        for j in range(N):
            print(table[N-j-1][i], end='')
        print(end=' ')

        for k in range(N):
            print(table[N-i-1][N-k-1], end='')
        print(end=' ')
        for l in range(N):
            print(table[l][N-i-1], end='')
        print()