import heapq

'''
10 14
0 1 12
0 2 15
1 3 4
1 4 10
2 5 7

8 9 5
'''
def dijkstra(start):
    # 출발점 설정
    dist[start] = 0
    heapq.heappush(heap, (dist[start], 0))
    # 모든 도시 선택될때까지
    for i in range(V):
        # # 최소값 찾기 (visit)
        # min = INF
        # u = -1
        # for v in range(V):
        #     if no visited[v] and dist[v] < min:
        #         min = dist[v]
        #         u = v
        # visited[u] = 1
        D, u = heapq.heappop(heap)
        if visited[u] : continue
        visited[u] = 1

        for v in range(V):
            if adj[u][v] and not visited[v]:
                if dist[v] > dist[u] + adj[u][v]:
                    dist[v] = dist[u] + adj[u][v]


        # 최소값 정점 인접한 정점 업데이트





V, E = map(int, input().split())    #정점, 간선
adj = [0] * V                        #인접행렬
INF = float('inf')
dist = [INF] * V                    # 가중치
visited = [0] * V                   # 방문여부
heap = []

for i in range():
    s, e, d = map(int, input().split())
    adj[s][e] = adj[e][s] = d

dijkstra(0)
print(dist)