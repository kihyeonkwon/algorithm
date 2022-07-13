tc= int(input())

for i in range (1, tc+1):
    result = {}
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    N, K=map(int, input().split())

    for j in range (1, N+1):
        a, b, c = map(int, input().split())
        result[j]=(0.35*a+0.45*b+0.2*c)
    
    ordered_values = sorted(result.values())
    ordered_values.reverse()
    students_per_grade = N/10
    K_students_rank = ordered_values.index(result[K])
    K_students_grade = grade[int(K_students_rank//students_per_grade)]
    print(f'#{i} {K_students_grade}') 
