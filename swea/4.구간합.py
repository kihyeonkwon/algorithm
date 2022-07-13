import sys
sys.stdin = open("구간합input.txt")
tc = int(input())

for i in range (1, tc+1):
    N, M = list(map(int, input().split()))
    number_list=list(map(int, input().split()))
    max_value = 0
    min_value=sum(number_list)
    for j in range(0, N-M+1):
        value = 0
        for k in range(M):
            value += number_list[j+k]

        if value > max_value:
            max_value = value

        if min_value>value:
            min_value = value

    print('#%d %d'%(i, max_value-min_value))
