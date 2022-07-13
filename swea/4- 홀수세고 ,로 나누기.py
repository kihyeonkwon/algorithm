a=range(1,100,2)
result=""

for i in a:
    result += "{0}, ".format(i)

print(result[0:len(result)-2])

