


def input_index():
    num = 0
    try:
        num =int(input("인덱스로 사용할 숫자를 입력하세요:"))
    except ValueError as exception:
        raise exception
    else:
        return num





data_list =list(range(1,11))





print(data_list)


try : 


    num =input_index()
    print("[{0}]: {1}".format(num, data_list[num]))

except IndexError as exception:
    print(exception)

except ValueError as exception:
    print("{0}, {1}".format(type(exception), exception))

except Exception as exception:
    print(exception)

