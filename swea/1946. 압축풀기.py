tc= int(input())

for i in range (1, tc+1):
    num = int(input())
    newstring = ""
    for j in range (num):
        a, b = input().split()
        b = int(b)
        newstring += a*b
    
    ent = len(newstring)//10

    print(f'#{i}')
    for j in range (1, ent+1):
        print (newstring[(10*j-10):10*j])

    print(newstring[10*(ent):])

print()