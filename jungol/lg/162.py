numbers = list(map(int, input().split()))

for i in range(8):
    numbers.append((numbers[i] + numbers[i+1]) %10)


for number in numbers:
    print(number, end=' ')