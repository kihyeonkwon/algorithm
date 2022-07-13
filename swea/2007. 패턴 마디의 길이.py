tc= int(input())

for v in range (1, tc+1):
    sample = input()
    
    for i in range (1, 11):
        a=0
        for j in range(10):
            if sample[j]==sample[j+i]:
                a+=1
            else:
                a+=0
            
        if a ==10:
            print(f'#{v} {i}')
            break



