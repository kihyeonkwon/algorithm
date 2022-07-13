table = [[3, 5, 9], [2, 11, 5], [8, 30, 10], [22, 5, 1]]


summed = 0
for row in table:
    for element in row:
        print(element, end=' ')
        summed += element
    print()
print(summed)