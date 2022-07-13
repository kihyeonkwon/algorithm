# import sys
# sys.stdin=open('스도쿠.txt')
#
# total_tc = int(input())
#
# for tc in range (1, total_tc+1):
#     table=[]
#     table = [(list(map(int, input().split()))) for _ in range(9)]
#
#
#     status = 1
#     loop1 = 0
#     loop2=0
#     loop3=0
#     while status==1:
#         for i1 in range (9):
#             sum=0
#             loop1 +=1
#             for j1 in range (9):
#                 sum+=table[i1][j1]
#
#             if sum !=45:
#                 status=0
#
#         if loop1==9:
#             break
#
#
#     while status ==1:
#         for j2 in range(9):
#             sum=0
#             loop2+=1
#             for i2 in range(9):
#                 sum +=table[i2][j2]
#             if sum != 45:
#                 status=0
#         if loop2==9:
#             break
#
#     while status ==1:
#         for i3 in range (0,7,3):
#             for j3 in range(0,7, 3):
#                 sum=0
#                 loop3 +=1
#                 for dx in range(3):
#                     for dy in range(3):
#                         sum += table[i3+dx][j3+dy]
#
#                 if sum!=45:
#                     status=0
#
#         if loop3 == 9:
#             break
#
#     if status ==1:
#         result = 1
#
#     else :
#         result = 0
#
#     print('#%d %d'%(tc,result))
#
#



#
T = int(input())

for t in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    result = 1
    for row in range(9):
        row_sum = 0
        col_sum = 0
        for col in range(9):
            row_sum += sudoku[row][col]
            col_sum += sudoku[col][row]
            if row % 3 == 0 and col % 3 == 0:
                squares = 0
                for i in range(3):
                    for j in range(3):
                        squares += sudoku[row + i][col + j]
                if squares != 45:
                    result = 0

        if row_sum != 45 or col_sum != 45:
            result = 0
    print('#{}'.format(t), result)



















import sys
sys.stdin = open('스도쿠.txt')

# 연속된 것들을 9개로 나눠줘야 한다.
sudoku = []
low = []
line = []
low_sums = []
low_multiples = []
line_sums = []
line_multiples = []
count = 0
x = 0
P = 0

A = []
B = []
for j in range(90):
    sudoku.append(list(map(int, input().split())))  # 2차원 배열 입력받는 9 X 90

for m in range(10):
    line_multiples = []
    line_sums = []
    low_multiples = []
    low_sums = []

    for k in range(x, x + 9):  # 가로로 9개 확인
        low_sum = 0
        low_multiple = 1
        for l in range(9):
            low_sum += sudoku[k][l]
            low_multiple *= sudoku[k][l]
        low_multiples.append(low_multiple)
        low_sums.append(low_sum)

    for n in range(9):  # 세로로 9개 확인
        line_sum = 0
        line_multiple = 1
        for o in range(x, x + 9):
            line_sum += sudoku[o][n]
            line_multiple *= sudoku[o][n]
        line_multiples.append(line_multiple)
        line_sums.append(line_sum)

    cell_multiples = []
    cell_sums = []
    for q in range(3):  # 세로로 3셀
        Q = 0
        for p in range(3):  # 가로로 3셀
            cell_sum = 0
            cell_multiple = 1
            for r in range(3):  # 한 셀안의 세로3셀
                for s in range(3):  # 한 셀안의 가로 3셀
                    cell_sum += sudoku[r + P][s + Q]
                    cell_multiple *= sudoku[r + P][s + Q]
            cell_sums.append(cell_sum)
            cell_multiples.append(cell_multiple)

            Q += 3
        P += 3
    if cell_sums == [45, 45, 45, 45, 45, 45, 45, 45, 45]:
        if cell_multiples == [362880, 362880, 362880, 362880, 362880, 362880, 362880, 362880, 362880]:
            if line_sums == [45, 45, 45, 45, 45, 45, 45, 45, 45]:
                if line_multiples == [362880, 362880, 362880, 362880, 362880, 362880, 362880, 362880, 362880]:
                    if low_sums == [45, 45, 45, 45, 45, 45, 45, 45, 45]:
                        if low_multiples == [362880, 362880, 362880, 362880, 362880, 362880, 362880, 362880, 362880]:
                            print(f'#{m + 1} 1')
                        else:
                            print(f'#{m + 1} 0')
                    else:
                        print(f'#{m + 1} 0')
                else:
                    print(f'#{m + 1} 0')
            else:
                print(f'#{m + 1} 0')
        else:
            print(f'#{m + 1} 0')
    else:
        print(f'#{m + 1} 0')

    x += 9