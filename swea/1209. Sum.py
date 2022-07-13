import sys
sys.stdin = open('input.txt')

total_tc = 10

for tc in range(1, total_tc+1):
    tc_number=int(input())
    table=[]
    for j in range (100):
        table.append(list(map(int, input().split())))

    max_values=[]
    for k1 in range (100):
        sum = 0
        for k2 in range (100):
            item = table[k1][k2]
            sum += item
        max_values.append(sum)

    for k1 in range (100):
        sum = 0
        for k2 in range (100):
            item = table[k2][k1]
            sum += item
        max_values.append(sum)

    for k1 in range (100):
        sum = 0
        for k2 in range (100):
            if k1==k2:
                item = table[k2][k1]
                sum += item
    max_values.append(sum)

    for k1 in range (100):
        sum = 0
        for k2 in range (100):
            if k1+k2==100:
                item = table[k2][k1]
                sum += item

    max_values.append(sum)



    print("#%d %d"%(tc, max(max_values)))
#
# for test_case in range(1, 11):
#     n = int(input())
#     box = [list(map(int, input().split())) for _ in range(100)]
#     box_col = [list(i) for i in zip(*box)]
#
#     box_sum = []
#     box_col_sum = []
#     dig1 = 0
#     dig2 = 0
#     for i in range(100):
#         box_sum.append(sum(box[i]))
#         box_col_sum.append(sum(box_col[i]))
#         dig1 += box[i][i]
#         dig2 += box[i][-(i + 1)]
#
#     print(f'#{test_case} {max([max(box_sum),max(box_col_sum),dig1,dig2])}')