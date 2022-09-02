a, b, c = map(int, input().split())




def my_func2(mult, result):
    value = mult//10
    remainder = mult % 10
    if value == 0 and remainder==0:
        print(result)
        return result
    else:
        if remainder != 0:
            my_func2(value, result*remainder)
        else:
            my_func2(value, result)


res = my_func2(1, 1)

print(res)







# def my_func(x, y , z):
#     value = x * y * z
#     value = str(value)
#     result =1
#     for number in value:
#         num = int(number)
#         if num != 0:
#             result *= num
#     return result
#
#
# print(my_func(a,b,c))
