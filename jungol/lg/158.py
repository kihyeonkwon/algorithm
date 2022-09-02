numbers = list(map(int, input().split()))

count = 0
for number in numbers:
    if number == 0:
        break
    count += 1

print(count)

for number in numbers:
    if number == 0:
        break
    if number %2 == 0:
        print(number//2, end=' ')
    else:
        print(number*2, end = ' ')


