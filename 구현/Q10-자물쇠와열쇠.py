def solution(key, lock):
    key_len = len(key)
    lock_len = len(lock)
    my_map = [[0]*(3*lock_len) for _ in range(3*lock_len)]  #3배의 크기의 자물쇠맵을 만들고 그 가운데에 기존의 자물쇠 생성
    for p in range(lock_len):
        my_map[lock_len+p][lock_len:2*lock_len] = lock[p]
    lock_list = []  # 자물쇠 위치인덱스 저장
    for m in range(lock_len, 2*lock_len):
        for n in range(lock_len, 2*lock_len):
            if my_map[m][n] == 0:
                lock_list.append([m, n])
    for _ in range(4):  # 오른쪽으로 90도 회전 3번
        key_list = []
        for i in range(key_len):  # 키의 위치인덱스를 저장
            for j in range(key_len):
                if key[i][j] == 1:
                    key_list.append([i, j])
        for p in range(3*lock_len - key_len + 1):
            for q in range(3*lock_len - key_len + 1):
                cnt = 0
                for key_x, key_y in key_list:
                    if my_map[key_x+p][key_y+q] == 1:
                        break
                    if [key_x+p, key_y+q] in lock_list:
                        cnt += 1
                if cnt == len(lock_list):
                    return True

        key = turn_right(key)
    return False

def turn_right(turn_key):
    a = [[] for _ in range(len(turn_key))]
    for l in range(len(turn_key)):
        a[l] = [turn_key[k][l] for k in range(len(turn_key)-1, -1, -1)]
    return a
