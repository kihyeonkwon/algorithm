import sys

sys.stdin = open("input.txt", "r")

s, e = map(int, input().split())

for idx in range(abs(s - e)+1):
    if s-e > 0:
        idx = idx * -1
    for num in range(1, 10):
        print(f"{s + idx} * {num} = {str((s + idx) * num).rjust(2)}", end="   ")
        if num % 3 == 0:
            print()
    print("")
