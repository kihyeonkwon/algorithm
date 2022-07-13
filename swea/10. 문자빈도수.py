a= input()



aset = set(a)

alist = sorted(list(aset))

datadic={}

for i in alist :
    datadic[i]=0
    for j in a :
        if i == j :
            datadic[i]+=1


for item in datadic.items():
    print("{0},{1}".format(item[0], item[1] ))