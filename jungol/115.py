min_h, min_w = map(int, input().split())
ki_h, ki_w = map(int, input().split())

if min_h > ki_h and min_w > ki_w :
    print(1)
else:
    print(0)