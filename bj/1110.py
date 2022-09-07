original_num = input()
if len(original_num) == 1:
    original_num = "0" + original_num


current_num = original_num
count = 0
while True:
    sum_num = int(current_num[0]) + int(current_num[1])
    sum_num = str(sum_num)
    current_num = current_num[-1] + sum_num[-1]
    count += 1
    if current_num == original_num:
        print(count)
        break
