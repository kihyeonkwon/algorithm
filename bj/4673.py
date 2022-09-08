def d(n):
    new_n = n
    for num in str(n):
        new_n += int(num)
    return new_n


all_numbers = [x for x in range(1, 10001)]

for i in range(1, 10001):
    not_a_self_number = d(i)
    if not_a_self_number in all_numbers:
        all_numbers.remove(not_a_self_number)


for number in all_numbers:
    print(number)
