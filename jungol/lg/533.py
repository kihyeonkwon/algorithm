sex, age = input().split()
age = int(age)


def person(sex, age):
    if sex == 'M' and age >=18:
        return "MAN"
    elif sex =='F' and age >=18:
        return "WOMAN"
    elif sex =="M" and age < 18:
        return "BOY"
    elif sex =="F" and age < 18:
        return "GIRL"
    else:
        print("error")

print(person(sex, age))