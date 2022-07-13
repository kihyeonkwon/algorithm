number = int(input())

table = [[0 for _ in range(number)] for _ in range(number)]



table[number-1][0] = 1

for i in range(number-2, -1, -1):
    for j in range(number):
        if j-1>=0:
            table[i][j] = table[i+1][j] + table[i+1][j-1]
        else:
            table[i][j] = table[i + 1][j]


for row in table:
    for element in row:
        if element != 0 :
            print(element, end=' ')
    print()