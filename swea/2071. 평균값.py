a = int(input())


for i in range (1, a+1):
    x = int(round(sum(map(int, input().split(' ')))/10, 0))
    print(f"#{i} {x}")