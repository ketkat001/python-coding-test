from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())
class_map = [list(input().split()) for _ in range(N)]
temp = []
teachers = []
for i in range(N):
    for j in range(N):
        if class_map[i][j] == 'X':
            temp.append([i, j])
        elif class_map[i][j] == 'T':
            teachers.append([i, j])
result = "NO"
for comb in combinations(temp, 3):
    cnt = 0
    for teacher in teachers:
        for d in range(4):
            next_x, next_y = teacher[0] + dx[d], teacher[1] + dy[d]
            while True:
                if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
                    break
                else:
                    if [next_x, next_y] in comb:
                        break
                    elif class_map[next_x][next_y] == 'S':
                        cnt += 1
                        break
                next_x += dx[d]
                next_y += dy[d]
            if cnt > 0:
                break
        if cnt > 0:
            break

    if cnt == 0:
        result = "YES"
        break
print(result)