import sys

sys.stdin = open("input.txt")

total_tc = 10

for tc in range(1, total_tc + 1):
    pali_len = int(input())
    table = [[input()] for _ in range(8)]
    count = 0

    for i in range(8 - pali_len + 1):
        for j in range(8):
            # 가로
            pali_x = []
            for k in range(pali_len):
                pali_x.append(table[i + k][0][j])

            if pali_x == pali_x[::-1]:
                count += 1

    for i in range(8):
        for j in range(8 - pali_len + 1):
            # 세로
            pali_y = []
            for l in range(pali_len):
                pali_y.append(table[i][0][j + l])
            if pali_y == pali_y[::-1]:
                count += 1

    print("#%d %d" % (tc, count))
