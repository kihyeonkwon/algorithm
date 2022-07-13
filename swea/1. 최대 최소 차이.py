import sys
sys.stdin = open("최대최소input.txt")


a= int (input())


for j in range (1, a+1):
    b = int(input())
    c = list(map(int, input().split(' ')))
    max_value=c[0]
    min_value=c[0]
    for i in c:
        if i>max_value:
            max_value=i
        if i<min_value:
            min_value=i
    d = max_value-min_value
    print('#%d %d'%(j, d))