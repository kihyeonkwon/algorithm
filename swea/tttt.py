

import sys

sys.stdin = open("스도쿠.txt")

trial = int(input())

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

for m in range(trial):
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