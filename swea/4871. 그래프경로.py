import sys

sys.stdin = open("그래프input.txt")

total_tc = int(input())


def DFS(S):
    visited[S] = True
    result = 0
    if S in valid:
        for Next in valid[S]:
            if not visited[Next]:
                if Next == G:
                    return 1
                elif not result:
                    result += DFS(Next)

    return result



for tc in range(1, total_tc+1):
    V, E = map(int, input().split())
    valid ={}
    result=0
    visited =[False for _ in range(V+1)]

    for _ in range(E):
        Start, End = map(int, input().split())
        if Start not in valid:
            valid[Start] = [End]
        else:
            valid[Start].append(End)

    S, G = map(int, input().split())
    print("#%d %d"%(tc, DFS(S)))

