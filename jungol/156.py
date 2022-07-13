numbers = list(map(int, input().split()))

max = 0
min = 0xffffff

for number in numbers:
    if number == 999:
        break
    if number > max:
        max = number
    if number < min:
        min = number

print('max : %d'%(max))
print('min : %d'%(min))