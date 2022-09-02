def exam(table):
    col_sum=[0, 0, 0]

    for i in range(3):
        row = 0
        for j in range(3):
            now_num = table[i][j]
            row += now_num
            col_sum[j] += now_num
            print(now_num, end=' ')
        print(row)

    for num in col_sum:
        print(num, end=' ')
    print(sum(col_sum))



table = [list(map(int, input().split())) for _ in range(3)]

exam(table)