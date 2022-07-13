import sys
sys.stdin = open('정렬input.txt')

total_tc = int(input())

for tc in range (1, total_tc+1):
    N = int(input())
    original_list = list(map(int, input().split()))

    #sort
    for i in range(N):
        min_value = 99999999
        max_value = 0

        index = 0
        if i % 2 == 0:
            for j in range(i, N):
                if original_list[j]>=max_value:
                    max_value = original_list[j]
                    index = j

            original_list[i] , original_list[index] = original_list[index],original_list[i]

        else:
            for j in range(i, N):
                if original_list[j] <= min_value:
                    min_value = original_list[j]
                    index = j

            original_list[i], original_list[index] = original_list[index], original_list[i]

    print('#%d'%(tc), end=' ')
    for i in range (10):
        print(original_list[i], end=' ')

    print()