import sys
sys.stdin = open('input.txt')

total_tc = 10

for tc in range(1, total_tc+1):
    total_dump = int(input())
    building_list = list(map(int, input().split()))
    number_of_buildings = len(building_list)
    building_dict={}
    for i in range(number_of_buildings):
        building_dict[i]=building_list[i]

    dump_count=0

    for j in range (total_dump):
        max_value = max(building_dict.values())
        min_value = min(building_dict.values())
        max_key = [k for k, v in building_dict.items() if v ==max_value]
        min_key = [k for k, v in building_dict.items() if v ==min_value]
        building_dict[max_key[0]]=building_dict[max_key[0]]-1
        building_dict[min_key[0]]=building_dict[min_key[0]]+1
        dump_count+=1
        if max(building_dict.values()) - min(building_dict.values()) == 1:
            break

    print('#%d %d'%(tc, max(building_dict.values()) - min(building_dict.values())))

#
# for test_case in range(1, 11):
#     count = int(input())
#     boxes = list(map(int, input().split()))
#
#     for i in range(count):
#         boxes[boxes.index(max(boxes))] -= 1
#         boxes[boxes.index(min(boxes))] += 1
#
#     print(f'#{test_case} {max(boxes) - min(boxes)}')




# 
# for t in range(1, 11):
#     N = int(input())
#     li = list(map(int, input().split()))
#     while max(li) - min(li) > 1 and N > 0:
#         li[li.index(max(li))] -= 1
#         li[li.index(min(li))] += 1
#         N -= 1
#     print(f'#{t} {max(li)-min(li)}')