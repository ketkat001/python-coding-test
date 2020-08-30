from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, K = map(int, input().split())
lab_map = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

queue = deque([])
for k in range(1, K+1):
    for i in range(N):
        for j in range(N):
            if lab_map[i][j] == k:
                queue.append([i, j])

while S > 0:
    temp_queue = deque([])
    while queue:
        v_x, v_y = queue.popleft()
        for d in range(4):
            next_x, next_y = v_x + dx[d], v_y + dy[d]
            if 0 <= next_x < N and 0 <= next_y < N:
                if lab_map[next_x][next_y] == 0:
                    lab_map[next_x][next_y] = lab_map[v_x][v_y]
                    temp_queue.append([next_x, next_y])
    queue = temp_queue
    S -= 1

print(lab_map[X-1][Y-1])