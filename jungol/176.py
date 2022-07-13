def count_between_sqaures(a, b):
    a1 = a**(1/2)
    b1 = b**(1/2)
    big = a1 if a1>b1 else b1
    small = b1 if a1>b1 else a1
    gap = int(big) - int(small)
    if small == int(small): gap += 1
    return int(gap)


a, b = map(float, input().split())



print(count_between_sqaures(a, b))