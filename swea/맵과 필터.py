#09-21




data_list = list(range(1, 21, 1))

print("data_list: {0}".format(data_list))


map_str = input("항목 x에 대해 적용할 표현식을 입력하세요: ")

map_list = list(map(lambda x: eval(map_str), data_list))




print(map_list)


filter_list = list(filter(lambda x: x%3==0 , map_list))


print(filter_list)