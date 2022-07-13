score = {'kor':90, 'mat':80, 'eng':100}

n = len(score)
sum = 0
for subject, score in score.items():
    sum += score
    print(subject, score)
avg = int(sum/n)
print('sum', sum)
print('avg', avg)
