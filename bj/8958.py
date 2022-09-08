T = int(input())


for _ in range(T):
    answers = input()
    total_score = 0
    point = 1
    for answer in answers:
        if answer == "O":
            total_score += point
            point += 1
        else:
            point = 1
    print(total_score)
