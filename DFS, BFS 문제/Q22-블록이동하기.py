from collections import deque


def solution(board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    start = {(0, 0), (0, 1)}
    queue = deque()
    queue.append((start, 0))
    N = len(board)
    visited = []
    visited.append(start)
    while queue:
        current_position, value = queue.popleft()
        current_position = list(current_position)
        if (N-1, N-1) in current_position:
            return value
        x1, y1 = current_position[0]
        x2, y2 = current_position[1]
        for d in range(4):  # 상하좌우 탐색
            n_x1, n_y1, n_x2, n_y2 = x1+dx[d], y1+dy[d], x2+dx[d], y2+dy[d]
            if 0 <= n_x1 < N and 0 <= n_x2 < N and 0 <= n_y1 < N and 0 <= n_y2 < N:  # 범위 안에 있고
                if board[n_x1][n_y1] != 1 and board[n_x2][n_y2] != 1:  # 벽이 아닌 경우
                    if {(n_x1, n_y1), (n_x2, n_y2)} not in visited:
                        visited.append({(n_x1, n_y1), (n_x2, n_y2)})
                        queue.append(({(n_x1, n_y1), (n_x2, n_y2)}, value+1))
        if x1 == x2:  # 로봇이 가로일 경우
            for s in [-1, 1]:  # 아래 위로 빈칸이 있을 경우 회전
                sx1, sx2 = x1+s, x2+s
                if 0 <= sx1 < N and 0 <= sx2 < N:
                    if board[sx1][y1] == 0 and board[sx2][y2] == 0:
                        if {(sx2, y2), (x2, y2)} not in visited:
                            visited.append({(sx2, y2), (x2, y2)})
                            queue.append(({(sx2, y2), (x2, y2)}, value+1))
                        if {(x1, y1), (sx1, y1)} not in visited:
                            visited.append({(x1, y1), (sx1, y1)})
                            queue.append(({(x1, y1), (sx1, y1)}, value+1))

        elif x1 != x2:  # 로봇이 세로일 경우
            for s in [-1, 1]:  # 양 옆으로 빈칸이 있을 경우 회전
                sy1, sy2 = y1+s, y2+s
                if 0 <= sy1 < N and 0 <= sy2 < N:
                    if board[x1][sy1] == 0 and board[x2][sy2] == 0:
                        if {(x2, sy2), (x2, y2)} not in visited:
                            visited.append({(x2, sy2), (x2, y2)})
                            queue.append(({(x2, sy2), (x2, y2)}, value+1))
                        if {(x1, y1), (x1, sy1)} not in visited:
                            visited.append({(x1, y1), (x1, sy1)})
                            queue.append(({(x1, y1), (x1, sy1)}, value+1))


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))