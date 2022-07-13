import sys
import itertools
sys.stdin = open('5188.txt')

TC = int(input())

def dfs(x, y, sum):
    if x == N-1 and y == N-1:
        return result.append(sum + table[x][y])
    else :
        sum += table[x][y]
        if x == N-1:
            dfs(x, y + 1, sum)
        elif y == N-1:
            dfs(x+1, y, sum)
        else:
            dfs(x+1, y, sum)
            dfs(x, y+1, sum)




for tc in range(1, TC+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    result = []
    dfs(0, 0, 0)
    print("#%d %d"%(tc, min(result)))



