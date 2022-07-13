tc= int(input())

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


for i in range (1, tc+1):
    days = 0
    m1, d1, m2, d2 = map(int, input().split())
    for j in range (m1-1, m2-1):
        days += month[j]

    days = days -d1 + d2 +1

    print(f'#{i} {days}')