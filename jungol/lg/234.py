N = int(input())


numbers = [1, 2]



def my_func(x):
    if x == N-2 :
        return
    numbers.append(numbers[x]*numbers[x+1]%100)
    my_func(x+1)


my_func(0)
print(numbers[-1])