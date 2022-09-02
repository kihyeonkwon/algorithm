ip = False
while not ip:
    a, b = map(int, input().split())
    if not 2<= a<=9 or not 2<=b<=9 :
        print("INPUT ERROR!")
    else:
        ip = True

d = 1
if a>b :
    d = -1

for i in range(1, 10):
    for j in range(a, b+d, d):
        print(f'{j} * {i} = {j*i if j*i>9 else " "+str(j*i)}', end = '   ' )
    print()