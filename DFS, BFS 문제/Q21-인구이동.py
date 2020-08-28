from collections import deque


def union(x, y, L, R):
    queue = deque([[x, y]])
    union_list = [[x, y]]
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        for d in range(4):
            next_x, next_y = x+dx[d], y+dy[d]
            if 0 <= next_x < N and 0 <= next_y < N:
                if visited[next_x][next_y] == 0 and L <= abs(country_map[x][y] - country_map[next_x][next_y]) <= R :
                    visited[next_x][next_y] = 1
                    union_list.append([next_x, next_y])
                    queue.append([next_x, next_y])
    temp = 0
    for country in union_list:
        temp += country_map[country[0]][country[1]]
    for country in union_list:
        country_map[country[0]][country[1]] = temp // len(union_list)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, L, R = map(int, input().split())
country_map = [list(map(int, input().split())) for _ in range(N)]
result = 0
while True:
    visited = [[0]*N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                for d in range(4):
                    next_x, next_y = i + dx[d], j + dy[d]
                    if 0 <= next_x < N and 0 <= next_y < N:
                        if visited[next_x][next_y] == 0 and L <= abs(country_map[i][j] - country_map[next_x][next_y]) <= R:
                            union(i, j, L, R)
                            flag = 1
                            break
    if flag == 0:
        break
    result += 1

print(result)