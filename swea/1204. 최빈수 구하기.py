a = int(input())


for i in range (1, a+1):
    tc = int(input())
    x = list(map(int, input().split()))
    res = max(set(x), key = x.count)
    print(f'#{tc} {res}') 

