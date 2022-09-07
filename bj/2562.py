num_list = []

for i in range(9):
    num_list.append(int(input()))


max_num = max(num_list)
index = num_list.index(max_num)

print(max_num)
print(index+1)
