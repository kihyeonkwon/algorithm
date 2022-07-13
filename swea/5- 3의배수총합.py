


a=range(1,101,1)
result=0


for i in a:
    if i%3==0:
        result+=i


print("1부터 100사이의 숫자 중 3의 배수의 총합: {0}".format(result))
