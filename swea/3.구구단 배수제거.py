
num_list = []
for i in range (2,10):
    jot = []
    for j in range (1,10):
        if i*j%3!=0 and i*j%7!=0:
            jot.append(i*j)


    num_list.append(jot)

print(num_list)