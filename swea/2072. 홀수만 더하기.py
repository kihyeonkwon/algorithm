a = int(input())


for i in range (1, a+1):
    x = list(map(int, input().split(' ')))
    result = 0
    for j in x:        
        if j %2 != 0:
            result += j
    print(f"#{i} {result}")