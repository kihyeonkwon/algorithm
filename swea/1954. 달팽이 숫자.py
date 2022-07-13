tc= int(input())


for i in range (1, tc+1):
    size = int(input())
    dx = [+1, 0, -1, 0]
    dy = [0, -1, 0, +1]




# num_of_case = int(input())
 
# for case_number in range(1, num_of_case + 1):
#     N = int(input())
#     matrix = [[0] * N for _ in range(N)]
#     matrix[0][0] = 1
 
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]
#     x = y = direction = 0
#     i = 2
 
#     while i <= N ** 2:
#         new_x = x + dx[direction % 4]
#         new_y = y + dy[direction % 4]
 
#         if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N or matrix[new_y][new_x] != 0:
#             direction += 1
#             continue
 
#         x = new_x
#         y = new_y
 
#         matrix[y][x] = i
#         i += 1
 
#     print('#{}'.format(case_number))
 
#     for row in matrix:
#         print(' '.join(map(str, row)))









# T = int(input())
# for n in range(T):
#     N = int(input())
#     snail = [[0 for x in range(N)] for y in range(N)]
#     p = N
#     x = 0
#     y = -1
#     d = 1
#     val = 1
#     while p >= 0:
#         for i in range(p):
#             y += d
#             snail[x][y] = val
#             val += 1
#         p -= 1
#         for i in range(p):
#             x += d
#             snail[x][y] = val
#             val += 1
#         d = d*-1
#     print(f'#{n+1}')
#     for i in range(N):
#         for j in range(N):
#             print(snail[i][j], end=' ')
#         print()