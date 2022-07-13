


data_str = "파이썬은 클래스를 이용해 객체를 생성하는 객체지향 프로그래밍 언어입니다."

find_str = "객체"

count = 0



idx=-1
while True :
    idx = data_str.find(find_str, idx + 1)
    if idx != -1:
        print("[{0}]~[{1}]".format(idx, idx + len(find_str)-1))
        new_str = data_str.replace(find_str, "****", count)
        print(new_str)
        count +=1
    else :
        break



print(idx)