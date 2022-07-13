tc= int(input())


for i in range (1, tc+1):
    h1, m1, h2, m2 = map(int, input().split())

    newh = h1 + h2
    newm = m1 + m2

    if newm > 60:
        newh +=1
        newm -= 60

    if newh > 12:
        newh -=12

    print(f'#{i} {newh} {newm}')