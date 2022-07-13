

a= list(map(int, input().split(', ')))


b = [i for i in a if i%2 !=0]



for j in b :
    if j != b[-1] :
        print("{0}".format(j), end=', ')
    else :
        print("{0}".format(j))



#         1
# 2
# 3
# 4
# a = input()
# t_list = list(map(int, a.split(', ')))
# result = [i for i in t_list if i & 1]
# print(', '.join(map(str, result)))
