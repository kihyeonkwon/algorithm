tc= int(input())

for i in range (1, tc+1):
    n = int(input())
    result=0
    for j in range (1, n+1):
        if j%2==0:
            result -= j
        else:
            result +=j

    print(f'#{i} {result}')
