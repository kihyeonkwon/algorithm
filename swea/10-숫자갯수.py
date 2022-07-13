# number=input()
# numberlist=[int(i) for i in str(number)]


# zero=0
# one=0
# two=0
# three=0
# four=0
# five=0
# six=0
# seven=0
# eight=0
# nine=0


# while len(numberlist)>0:
#     a=int(numberlist.pop())
#     if a==0:
#         zero+=1
#     if a==1:
#         one+=1
#     if a==2:
#         two+=1
#     if a==3:
#         three+=1
#     if a==4:
#         four+=1
#     if a==5:
#         five+=1
#     if a==6:
#         six+=1
#     if a==7:
#         seven+=1
#     if a==8:
#         eight+=1
#     if a==9:
#         nine+=1


# print("0 1 2 3 4 5 6 7 8 9")
# print("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}".format(zero, one, two, three, four, five, six, seven, eight, nine))


a = str(input())
numlist = list(range(0, 10))
blist = [0]*10
for i in numlist:
    for j in a:
        if i == int(j):
            blist[i] += 1
print(' '.join(map(str, numlist)))
print(' '.join(map(str, blist)))
