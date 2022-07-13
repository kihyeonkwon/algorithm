import sys
sys.stdin = open('행렬input.txt')

total_tc = int(input())

for tc in range (1, total_tc):
    N = int(input())
    table = [[list(map(int, input().split()))] for _ in range (N)]
    dx
    for i in range (N):
        for j in range (N):
            countx = 0
            county = 0
            if table[i][j] != 0:
                for k in range(i, N):
                    if table[k][j]!=0:
                        county+=1
                for l in range(j, N):
                    if table[i][l] !=0:
                        countx +=1




    print(table)
