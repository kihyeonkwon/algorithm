numbers = list(map(int, input().split()))

for i in range(1, 7):
    print('%d : %d'%(i, numbers.count(i)))