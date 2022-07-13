import sys
sys.stdin = open('input.txt')


def maze_runner(maze, TF, N):
    start_x = maze[N-1].index(2)
    end_x = maze[0].index(3)


T = int(input())
N = int(input())
maze = [list(input()) for _ in range (N)]
TF = [[False for _ in range (N)] for _ in range(N)]

print(TF)