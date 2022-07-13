n = int(input())

for i in range (1, n+1):
    p, q, r, s, w = map(int, input().split())
    a = p * w
    if w <= r :
        b = q
    else:
        b = q + (w-r)*s

    if a<=b :
        print(f'#{i} {a}')
    else:
        print(f'#{i} {b}')
