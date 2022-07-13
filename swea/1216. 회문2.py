import sys

sys.stdin = open('회문2input.txt')


def palindrome(table, N):
    max_value=0
    for M in range(N, 0, -1):
        for i in range (N):
            for j in range(N-M+1):
                count = 0
                for k in range(M//2):
                    if table[i][j+k]==table[i][j+M-k-1]:
                        count +=1
                if count == M//2:
                    if M>max_value:
                        max_value=M

        for i in range (N):
            for j in range(N-M+1):
                count = 0
                for k in range(M//2):
                    if table[j+k][i]==table[j+M-k-1][i]:
                        count +=1
                if count == M//2:
                    if M>max_value:
                        max_value=M

    return max_value





total_tc = 10

for tc in range(1, total_tc+1):
    tc_input=int(input())
    table = [list(input()) for _ in range (100)]
    print("#%d %d"%(tc, palindrome(table, 100)))

T = 10


# def findP(mat):
#     temp = ''
#     for n in range(101, 1, -1):
#         for i in range(100):
#             for j in range(101 - n):
#                 s = mat[i][j:j + n]
#                 temp = ''
#                 if s == s[::-1]:
#                     return n
#                 for k in range(n):
#                     temp += mat[j + k][i]
#                 if temp == temp[::-1]:
#                     return n
#     return 0
#
#
# for test_case in range(1, T + 1):
#     t = int(input())
#     mat = []
#     for _ in range(100):
#         mat.append(input())
#     print(f'#{t} {findP(mat)}')
