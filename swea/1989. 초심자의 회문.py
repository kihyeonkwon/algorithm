tc= int(input())

for j in range (1, tc+1):
    x = input()
    a=0
    for i in range (len(x)):
        if x[i]==x[-i-1]:
            a +=0
        else:
            a+=1

    if a ==0:
        result=1
    else:
        result =0

    print(f'#{j} {result}')