num = int(input())

count = 1
while True:
    new_num = num*count
    if new_num >100:
         break
    print(new_num, end=" ")
    if new_num%10 ==0:
        break
    count += 1
