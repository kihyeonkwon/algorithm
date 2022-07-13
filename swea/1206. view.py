tc= 10

for v in range (1, tc+1):
    number_of_buildings = int(input())
    building_list = list(map(int, input().split()))
    count = len(building_list)
    total = 0

    for i in range (2, count-2):
        #왼쪽조망권
        left=0
        if building_list[i]>building_list[i-1] and building_list[i]>building_list[i-2]:
            left = 1

        #오른쪽조망권
        right=0
        if building_list[i]>building_list[i+1] and building_list[i]>building_list[i+2]:
            right = 1

        if left ==1 and right ==1:
            #조망권 확보된 층수 구하기
            #가장 높은 나머지 네개
            view = building_list[i]-max([building_list[i-2], building_list[i-1], building_list[i+1], building_list[i+2]])
            total += view
            yorn =1
        

    print(f'#{v} {total}')