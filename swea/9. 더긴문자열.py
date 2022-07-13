# a = input().split(', ')

# if len(a[0]) > len(a[1]):
#     print(a[0])

# else :
#     print(a[1])



a = input().split(', ')
b=len(a)
newlist=[]
d=0


for i in range (0, b):
    newlist+=[len(a[i])]


c= int(max(newlist))



for i in range (0, b):
    if newlist[i]==c:
        d=i
    
print(a[d])

