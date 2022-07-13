# def calc_sum(precision, *params):
#     if precision == 0:
#         total = 0
        
#     elif 0< precision <1:
#         total = 0.0


    

#     for val in params:
#         total += val
#     return total

# ret_val = calc_sum(0.1, 1.45, 2.62)

# print("calc_sum(0, 1, 2)함수가 반환한 값: {0}".format(ret_val))









# def use_keyword_arg_unpacking(**params):
#     for k in params.keys():
#         print("{0}: {1}".format(k, params[k])




# print("use_keyword_arg_unpacking()의 호출")
# use_keyword_arg_unpakcing(a=1, b=2, c=3)




def calc(x, y, operator="+"):
    if operator == "+":
        return x+y
    else:
        return  x-y


ret_val = calc(10, 5, "+")
print("calc(10, 5, +)의 결과 값 : {0}".format(ret_val))