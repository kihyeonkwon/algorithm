height, weight = map(int, input().split())
obesity = weight + 100 - height

print("%d"%(obesity))
if obesity>0:
    print("Obesity")
