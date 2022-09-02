inventory = [['item', 'count', 'price'], ['pen', 20, 100], ['note', 5, 95], ['eraser', 110, 97]]

for item in inventory:
    for value in item:
        print("{0:>10}".format(value), end='')
    print()


