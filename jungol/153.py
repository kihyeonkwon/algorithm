nums = list(map(int, input().split()))

for i in range(len(nums)):
    if nums[i]== -1:
        if i<3:
            for j in range(i):
                print(nums[j], end=' ')
        else:
            for j in range(i-3, i):
                print(nums[j], end=' ')

