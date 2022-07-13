# 1에서 100까지 숫자 중 n의 배수 구하기

n=int(input())

x = list(range(1, 101))

y = list(filter(lambda z: z%n==0, x))


print(y)