# Q11-뱀

def change_direction(change, d):
    if change == 'D':
        if d == 0:
            direction = 3
        elif d == 1:
            direction = 2
        elif d == 2:
            direction = 0
        else:
            direction = 1
    else:
        if d == 0:
            direction = 2
        elif d == 1:
            direction = 3
        elif d == 2:
            direction = 1
        else:
            direction = 0
    return direction


def solution(s_x, s_y, di):
    global time
    map_list[s_x][s_y] = 1
    tail_list = [[s_x, s_y]]  # 머리가 지나간 길을 저장 ( 꼬리를 없애주기 위해 )
    while True:
        time += 1
        next_x, next_y = s_x + dx[di], s_y + dy[di]
        if 0 <= next_x < N and 0 <= next_y < N:
            if map_list[next_x][next_y] == 1:
                break
            elif map_list[next_x][next_y] == 0:
                e_x, e_y = tail_list.pop(0)
                map_list[next_x][next_y] = 1
                tail_list.append([next_x, next_y])
                map_list[e_x][e_y] = 0
                s_x, s_y = next_x, next_y
            elif map_list[next_x][next_y] == 3:
                map_list[next_x][next_y] = 1
                tail_list.append([next_x, next_y])
                s_x, s_y = next_x, next_y

        else:
            break
        for i in range(L):
            if int(di_change[i][0]) == time:
                di = change_direction(di_change[i][1], di)
    return


dx = [0, 0, -1, 1]  # 우 좌 상 하
dy = [1, -1, 0, 0]

N = int(input())
K = int(input())
map_list = [[0]*N for _ in range(N)]
for _ in range(K):
    a_x, a_y = map(int, input().split())
    map_list[a_x-1][a_y-1] = 3  # 사과 인덱스의 시작은 1이고 코드는 0으로 시작하기 때문에 1을 빼줌
L = int(input())
di_change = []
for _ in range(L):
    di_change.append(list(input().split()))

time = 0
solution(0, 0, 0)
print(time)