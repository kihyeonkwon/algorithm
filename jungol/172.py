def square_maker(num):
    table = [[0 for _ in range(num)] for _ in range(num)]
    for i in range(num):
        for j in range(num):
            table[i][j] = (i+1)*(j+1)
    return table

table = square_maker(int(input()))


for row in table:
    for element in row:
        print(element, end=' ')
    print()