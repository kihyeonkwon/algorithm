import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    scores = input()
    lost = 0
    possible = 'YES'
    for score in scores:
        if score == 'x':
            lost += 1
    if lost > 7:
        possible = 'NO'
    print(f'#{test_case} {possible}')
