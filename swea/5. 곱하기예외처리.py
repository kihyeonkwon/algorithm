a = input().split(', ')
result=1



try :
    b=len(a)

    for i in range (b):
        result=result*int(a[i])

    print(result)


except:
    print('에러발생')