tc= int(input())


for i in range (1, tc+1):
    max = 0


    n, m = map(int, input().split())
    a = list(input().split())
    b = list(input().split())

    if n>m:
        for k in range (n-m+1):
            total = 0
            for j in range (m):
                total += int(b[j]) * int(a[j+k])
            if total >max :
                max = total

    elif n<m :
        for k in range (m-n+1):
            total = 0
            for j in range (n):
                total += int(a[j]) * int(b[j+k])
            if total >max :
                max = total


    print(f'#{i} {max}')

