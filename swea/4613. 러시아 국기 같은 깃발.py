import sys
sys.stdin = open('4613.txt')


total_tc = int(input())

for tc in range(1, total_tc+1):
    N, M = map(int, input().split())
    flag = [[x for x in input()] for _ in range (N)]
    count = 0
    min_count = 10000000
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                count = 0
                for x in range(M):
                    if flag[i][x] != 'W':
                        count +=1
                    if flag[j][x] != 'B':
                        count +=1
                    if flag[k][x] != 'R':
                        count +=1
                print(i,j, k)
                print(count)
                if count < min_count:
                    min_count=count

    print('#%d %d'%(tc, min_count))

