import sys
sys.stdin = open('5249.txt')


def dfs():



TC = int(input())
TC = 1
for tc in range(1, TC +1):
    V, E = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(E)]
    print(table)
