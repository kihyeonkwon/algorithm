a = int(input())

for i in range(1, a+1):
    a, b = map(int, input().split())
    x, y = divmod(a, b)
    print(f'#{i} {x} {y}')