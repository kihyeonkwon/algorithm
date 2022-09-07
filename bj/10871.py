N, X = map(int, input().split())

my_list = list(map(int, input().split()))


result_list = []
for number in my_list:
    if number < X:
        result_list.append(str(number))

print('aaa'.join(result_list))
