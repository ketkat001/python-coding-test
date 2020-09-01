def solution(current, num):
    global cnt
    if len(current) < 1:
        return
    start = 0
    end = len(current)-1
    mid = start+end // 2
    if current[mid] == num:
        cnt += 1
        solution(current[:mid], num)
        solution(current[mid+1:end+1], num)
    elif current[mid] > num:
        solution(current[:mid], num)
    else:
        solution(current[mid+1:end+1], num)


N, x = map(int, input().split())
a_list = list(map(int, input().split()))
cnt = 0
solution(a_list, x)
if cnt == 0:
    print(-1)
else:
    print(cnt)
