target = int(input())
repeat = 0
count = 0
while True:
    x = 0
    y = repeat
    for i in range(repeat):
        count += 1
        y -= 1
        x += 1
        if count == target:
            break
    if count == target:
        print(f"{x}/{y}")
        break
    repeat += 1
