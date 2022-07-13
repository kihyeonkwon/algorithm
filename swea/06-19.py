#06-19 오하년


a=int(input("첫 번째 숫자를 입력하세요:"))

b=(input("연산자를 입력하세요:"))

c=int(input("두 번째 숫자를 입력하세요"))

if b=='+':
    d=a+c
    print("%d + %d = %d"%(a, c, d))

elif b=='-':
    d=a-c
    print("%d - %d = %d"%(a, c, d))

elif b=='*':
    d=a*c
    print("%d * %d = %d"%(a, c, d))

elif b=='/':
    d=a/c
    print("%d / %d = %.2f"%(a, c, d))

else:
    print("'%s'는 프로그램에서 지원하지 않는 연산자입니다. "%(b))