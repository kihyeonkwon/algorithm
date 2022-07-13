N = int(input())

count = 0
def div2or3(x):
    global count


    if x==1:
        return
    count += 1

    if x%2 ==0 :
        div2or3(int(x/2))
    else:
        div2or3(int(x/3))

div2or3(N)
print(count)