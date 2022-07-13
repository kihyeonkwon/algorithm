count = 0
while True : 
    a = input()
    if not a :
        break

    print(">> {0}".format(a.upper()))
    count +=1
    if count ==3 :
        break