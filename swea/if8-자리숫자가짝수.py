a=100
result=''





while a<=300:

    q=int(str(a)[0])
    w=int(str(a)[1])
    e=int(str(a)[2])

    if (q%2==0 and w%2==0 and e%2==0):
        result+='%d,'%a
        a+=1
    
    else:
        a+=1


if a==301:
    print(result[0:len(result)-1])