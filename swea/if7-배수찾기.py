a=1
result=''


while a<=200:

    if (a%7==0 and a%5!=0):
        result += "%d,"%a
        a+=1

    else:
        a+=1

if a==201:
    print(result[0:len(result)-1])