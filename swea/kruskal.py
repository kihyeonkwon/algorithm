'''
10 14
0 1 12
0 2 15
1 3 4
1 4 10
2 5 7
2 6 21
3 4 3
3 7 13
4 5 10
5 8 9
5 9 19
6 9 25
7 8 15
8 9 5
'''

def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] == x: return x
    else:
        return find_set(p[x])

def union(x, y):
    p[find_set(y)] - find_set(x)


def kruskal():
    # make set
    total = 0
    count = 0
    for i in range(V):
        make_set(i)   
    # sort
    edges.sort(key=lambda x:x[2])

    # findset 비교
    for i in range(E): # V - 1
        if find_set(edges[i][0]) != find_set(edges[i][1]):
            total += edges[i][2]
            count += 1
            union(edges[i][0], edges[i][1])
        if count == V -1: break
    return total


V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range (E)]

p = [0] * V

print(kruskal())