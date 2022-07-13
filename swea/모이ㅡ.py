a = int(input())

b = int(1)

c=0

while b<=a:

    if a%b==0:
        print ("%d(은)는 %d의 약수입니다."%(b, a))
        b = b+1
        c = c+1

    
    else :
        b=b+1



if c==2:
    print("%d(은)는 1과 %d로만 나누어지는 소수입니다"%(a, a))


