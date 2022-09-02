table = [[1, 0, 1, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for i in range(1, 5):
    for j in range(5):
        front = 0
        back = 0
        if j-1>= 0 :
            front = table[i-1][j-1]
        if j+1 < 5:
            back = table[i-1][j+1]
        table[i][j] = front + back

for row in table:
    for element in row:
        print(element, end = ' ')
    print()