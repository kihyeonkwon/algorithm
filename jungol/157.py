numbers = list(map(int, input().split()))


mult5 = []

for number in numbers:
    if number == 0:
        break
    if number%5==0:
        mult5.append(number)

count = len(mult5)

print('Multiples of 5 : %d'%(count))
print('sum : %d'%(sum(mult5)))
print('avg : %.1f'%(sum(mult5)/count))