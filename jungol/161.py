numbers = list(map(int, input().split()))



count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for number in numbers:
    score = number//10
    if number == 0:
        break
    else:
        count[score] += 1

for i in range(10, -1, -1):
    now_count = count[i]
    if now_count != 0:
        print("%d : %d person"%(i*10, now_count))
