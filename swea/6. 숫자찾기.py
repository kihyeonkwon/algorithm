a = [2, 4, 6, 8, 10]


print (a)


def findnumbertrue(x):
    for i in range(0, 5):
        if a[i] ==x:
            print("{0} => True".format(x))


def findnumberfalse(y):
    c=0
    for i in range(0, 5):
        if a[i] !=y:
            c=c+1

    if c==5:
        print("{0} => False".format(y))



findnumberfalse(5)
findnumbertrue(10)


