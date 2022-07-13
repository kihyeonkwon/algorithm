import sys

sys.stdin = open('input.txt')

def palindrome(table, N, M):
    for i in range (N):
        for j in range(N-M+1):
            count = 0
            for k in range(M//2):
                if table[i][j+k]==table[i][j+M-k-1]:
                    count +=1
            if count == M//2:
                return i,j,+1

    for i in range (N):
        for j in range(N-M+1):
            count = 0
            for k in range(M//2):
                if table[j+k][i]==table[j+M-k-1][i]:
                    count +=1
            if count == M//2:
                return j,i,-1





total_tc = int(input())


for tc in range(1, total_tc+1):
    N, M = map(int, input().split())
    table=[input() for _ in range (N)]
    i,j,c = palindrome(table, N, M)
    result=[]
    if c==1:
        for k in range(M):
            result.append(table[i][j+k])
    else:
        for k in range(M):
            result.append(table[i+k][j])

    result=''.join(result)


    print('#%d %s'%(tc, result))