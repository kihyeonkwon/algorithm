n = int(input())

count = 1

for i in range(n):
    for j in range(n):
        print(count, end=' ')
        count = (count+2)%10
    print()