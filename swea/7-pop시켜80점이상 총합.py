score=[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
result=0


while len(score)>=1:
    a=score.pop()
    if a>= 80:
        result += a


print(result)
