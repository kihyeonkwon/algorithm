a, b, c = 2, 3, 4

result=[]


for i in range (a):
    temp1 =[]
    
    for j in range (b):
        temp2 = []
        for k in range (c):
            temp2.append(0)
        temp1 = temp1 +[temp2]
    
    result = result +[temp1]


print(result)