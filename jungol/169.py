table = []
for i in range(3):
    table.append(list(input().split()))

for row in table:
    for element in row:
        print(element.lower(), end=' ')
    print()