classes = []

for i in range(1, 5):
    classes.append(list(map(int, input("%dclass? "%(i)).split())))


for i in range(1, 5):
    print("%dclass : %d"%(i, sum(classes[i-1])))