tc= int(input())


for i in range (1, tc+1):
    total_second = int(input())
    distance = 0
    speed = 0
    for j in range(total_second):

        li= list(input().split())

        if int(li[0])==1:
            speed += int(li[1])

        elif int(li[0]) == 2:
            speed -= int(li[1])
            if speed < 0 :
                speed = 0

        
        distance += speed


    print(f'#{i} {distance}')
