import sys
sys.stdin = open('1247.txt')

TC = int(input())

def distance(here, there):
    dist = abs(there[0] - here[0]) + abs(there[1] - here[1])
    return dist


def travel(location, sum):
    global min_sum
    global N
    if sum > min_sum :
        return 1
    if False not in visited[2:]:
        sum += distance(new_coor[location], new_coor[1])
        min_sum = min(sum, min_sum)
        return 1
    for i in range(2, N):
        if not visited[i]:
            visited[i] = True
            travel(i, sum + distance(new_coor[location], new_coor[i]))
            visited[i] = False



for tc in range(1, TC + 1):
    N = int(input())
    coor = list(map(int, input().split()))
    new_coor = []
    for i in range(0, len(coor), 2):
        new_coor.append([coor[i], coor[i+1]])
    N = len(new_coor)
    visited = [False for _ in range (N)]
    min_sum = 0xffffff
    travel(0, 0)
    print("#%d"%(tc), min_sum)



