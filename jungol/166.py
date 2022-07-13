table= [[], []]

for i in range(2):
    table[i].append(list(map(int, input().split())))
    table[i].append(list(map(int, input().split())))


result = [[], []]

for i in range(2):
    for j in range(3):
        result[i].append(table[1][i][j]*table[0][i][j])



print('first array')
print('second array')
for row in result:
    for element in row:
        print(element, end=' ')
    print()