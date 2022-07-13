n = int(input())

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
count_a = 0
count_n = 0

for i in range(n):
    for j in range(n-i):
        print(alphabet[count_a], end=' ')
        count_a += 1
    for j in range(i):
        print(count_n, end=' ')
        count_n += 1

    print()