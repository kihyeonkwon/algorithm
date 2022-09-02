numbers = list(map(int, input().split()))

n = len(numbers)
odd_sum = 0
even_sum = 0

for i in range(n):
    if i%2 == 0:
        odd_sum += numbers[i]
    else:
        even_sum += numbers[i]

print('odd : %d'%(odd_sum))
print('even : %d'%(even_sum))