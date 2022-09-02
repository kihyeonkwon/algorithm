a, b = map(int, input().split())

big = a if a>b else b
small = b if a>b else a

sum = 0
count = 0

for i in range(small, big+1):
    if i%3==0 or i%5 ==0:
        count += 1
        sum += i
    else:
        pass

avg = round(sum/count, 1)
print("sum : %d"%(sum))
print("avg : %.1f"%(avg))