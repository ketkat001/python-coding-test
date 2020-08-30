from itertools import combinations
from collections import deque
import copy


def check_virus(lab_map, wall, st):
    global max_val
    lab_m = copy.deepcopy(lab_map)
    for w_x, w_y in wall:
        lab_m[w_x][w_y] = 1
    queue = deque(st)
    while queue:
        v_x, v_y = queue.popleft()
        for d in range(4):
            next_x, next_y = v_x + dx[d], v_y + dy[d]
            if 0 <= next_x < N and 0 <= next_y < M:
                if lab_m[next_x][next_y] == 0:
                    lab_m[next_x][next_y] = 2
                    queue.append([next_x, next_y])
    cnt = 0
    for n in range(N):
        for m in range(M):
            if lab_m[n][m] == 0:
                cnt += 1
    if cnt >= max_val:
        max_val = cnt


dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
labo_map = [list(map(int, input().split())) for _ in range(N)]
temp = []
start = []
max_val = 0
for i in range(N):
    for j in range(M):
        if labo_map[i][j] == 0:
            temp.append([i, j])
        elif labo_map[i][j] == 2:
            start.append([i, j])

for add_wall in combinations(temp, 3):
    check_virus(labo_map, add_wall, start)

print(max_val)