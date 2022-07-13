table  = []

for i in range(4):
    table.append(list(map(int, input().split())))

row_sum = [0, 0, 0, 0]
col_sum = [0, 0]
total_sum = 0

for i in range(4):
    for j in range(2):
        number = table[i][j]
        row_sum[i] += number
        col_sum[j] += number
        total_sum += number


for number in row_sum:
    print('%d'%(number//2), end= ' ')
print()
for number in col_sum:
    print('%d'%(number//4), end= ' ')
print()

print('%d'%(total_sum//8))

