a, b = map(int, input().split())

incline = 1 if a < b else -1

for i in range(1, 10):
    for j in range(a, b + incline, incline):
        print("%d * %d = %2d"%(j, i, j*i), end="   ")
    print()
