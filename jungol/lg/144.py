num = int(input())

totalNum = num*2 - 1

for i in range(1, num+1):
    print(" "*(totalNum - (2*i-1)), end="")
    print("*"*(2*i-1))