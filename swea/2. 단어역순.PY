# a = input ()



# b = a.split( )

# print(b)


# c = len(b)

# for i in range (c-1, -1, -1):
#     print("{0}".format(b[i]), end=" ")



# 다음과 같이 문장을 구성하는 단어를 역순으로 출력하는 프로그램을 작성하십시오.
# A better tomorrow

a = input()
b = a.split(" ")
print(" ".join(b[::-1]))