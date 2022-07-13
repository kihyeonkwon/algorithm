tc= int(input())


for i in range (1, tc+1):
    size = int(input())
    num_list = list(map(int, (input().split())))
    num_list.sort()
    print(f'#{i}', end=' ')
    for j in range (size):
        print(f'{num_list[j]}', end=' ')
    print()