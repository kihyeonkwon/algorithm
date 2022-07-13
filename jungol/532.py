a, b = map(float, input().split())


def score(a, b):
    if a>=4.0 and b >= 4.0:
        return "A"
    elif a>=3.0 and b >= 3.0:
        return "B"
    else :
        return "C"

my_score = score(a, b)
print(my_score)
