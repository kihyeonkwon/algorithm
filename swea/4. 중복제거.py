a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900,
     '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}


b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}


# 중복제거
for i in a:
    b[i] = a[i]


c = set()

for i in b:

    if b[i] > 3000:
        tuple1 = (i, b[i])
        c.add(tuple1)


print(c)
