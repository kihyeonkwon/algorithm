t = int(input())

for i in range(1, t + 1):
    n = int(input())

    table = [list(map(int, input().split())) for _ in range(n)]
    chemicals = []
    for y in range(n):
        for x in range(n):
            s = 0
            if table[y][x] != 0:
                if y > 0 and x > 0:
                    if table[y - 1][x] == 0 and table[y][x - 1] == 0:
                        s = 1
                elif x == 0 and y > 0:
                    if table[y - 1][x] == 0:
                        s = 1
                elif x > 0 and y == 0:
                    if table[y][x - 1] == 0:
                        s = 1
                else:
                    s = 1

            if s == 1:
                tx = x
                ty = y
                while tx < n and table[y][tx] != 0:
                    tx += 1
                while ty < n and table[ty][x] != 0:
                    ty += 1
                lx = tx - x
                ly = ty - y
                chemicals.append([lx * ly, ly, lx])

    for j in range(len(chemicals)):
        for k in range(0, len(chemicals) - j - 1):
            if chemicals[k][0] > chemicals[k + 1][0]:
                chemicals[k], chemicals[k + 1] = chemicals[k + 1], chemicals[k]
            elif chemicals[k][0] == chemicals[k + 1][0] and chemicals[k][1] > chemicals[k + 1][1]:
                chemicals[k], chemicals[k + 1] = chemicals[k + 1], chemicals[k]

    print(f'#{i} {len(chemicals)}', end=" ")
    for c in chemicals:
        print(c[1], c[2], end=" ")
    print()