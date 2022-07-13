a=[1, 2, 3, 4, 5, 6 , 7, 8, 9, 10]


even_a = filter (lambda x: x%2==0, a)

squa_a = list(map (lambda y: y**2, even_a))


print(squa_a)