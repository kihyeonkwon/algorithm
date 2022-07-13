import sys
sys.stdin = open('4875.txt')

TC = int(input())
for tc in range(1, TC +1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    maze_tf = [[0 for _ in range(N)] for _ in range(N)]
    #startpoint (y, x)

    for i in range(N):
        for j in range(N):
            if maze[j][i] == 2:
                startpoint = (j, i)
            if maze[j][i] == 3:
                endpoint = (j, i)


    #travel via bfs
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    Q = []

    Q.append(startpoint)
    result = 0
    while Q:

        now = Q.pop(0)
        maze_tf[now[0]][now[1]] = 1
        for d in range(4):
            next = (now[0]+dy[d], now[1]+dx[d])
            if 0 <= next[0] < N and 0 <= next[1] < N:

                if maze_tf[next[0]][next[1]] == 0:
                    if maze[next[0]][next[1]] == 3:
                        result =1
                    elif maze[next[0]][next[1]] == 0:
                        Q.append(next)
    print('#%d %d'%(tc, result))

