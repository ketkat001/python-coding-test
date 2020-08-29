N = int(input())
student_score = []
for _ in range(N):
    name, score1, score2, score3 = input().split()
    student_score.append([name, int(score1), int(score2), int(score3)])

result = sorted(student_score, key=lambda x:(-x[1], x[2], -x[3], x[0]))
for i in range(N):
    print(result[i][0])