student1 = (90, 80)
student2 = (85, 75)
student3 = (90, 100)

scores=[]

scores.append(student1)
scores.append(student2)
scores.append(student3)



for i, score in enumerate(scores, 1) :
    total = 0
    for s in score :
        total += s
    print("{0}번 학생의 총점은 {1}점이고, 평균은 {2:0.1F}입니다.".format(i, total, total / len(score)))