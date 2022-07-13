import sys

sys.stdin = open('input.txt')

total_tc = int(input())



for tc in range (1, total_tc+1):
    N, K = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]
    ans = []

    for i in range(N):
        cntx = 0
        cnty = 0
        for j in range(N):
            if table[j][i] ==1:
                cntx+=1
            else:
                ans.append(cntx)
                cntx=0

            if table[i][j] == 1:
                cnty += 1
            else:
                ans.append(cnty)
                cnty =0
        ans.append(cntx)
        ans.append(cnty)


    print("#%d %d"%(tc, ans.count(K)))