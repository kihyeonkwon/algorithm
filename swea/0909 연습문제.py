# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

def preorder(node):
    global cnt
    if node:
        cnt += 1
        print(node, end = ' ')
        preorder(tree[node][0])
        preorder(tree[node][1])



V = int(input())
E = V - 1
tree = [[0, 0, 0] for _ in range(V+1)]
relations = list(map(int, input().split()))
for i in range(V-1):
    parent, child = relations[2*i:2*i+2]
    if tree[parent][0]==0:
        tree[parent][0] = child
    else:
        tree[parent][1] = child
    tree[child][2]=parent



for t in tree:
    print(*t)

cnt = 0
preorder(1)

print(cnt)