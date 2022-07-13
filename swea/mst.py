def prim(start):
    total = 0 #가중치의 합
    u = start
    dist[u] = 0
    for i in range(V):
        # 최소값 정점
        min = INF
        u = -1 #안써도대긴함 어차피 구해져서
        for v in range(V):
            if not visited[v] and min > dist[v]:
                min = dist[v]
                u = v
        # 방문체크
        visited[u] = True
        total += adj[PI[u]][u]
        # 업데이트
        for v in range(V):
            if adj[u][v] != 0 and visited[v] == 0 and adj[u][v] < dist[v]:
                dist[v] = adj[u][v]
                PI[v] = u

        return total








V, E = map(int, input().split())    #정점, 간선
adj = [0] * V                        #인접행렬
INF = float('inf')
dist = [INF] * V                    # 가중치
visited = [0] * V                   # 방문여부
PI = list(range(V))

for i in range():
    s, e, d = map(int, input().split())
    adj[s][e] = adj[e][s] = d