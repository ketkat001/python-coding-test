def solution(current, start, end):
    global answer
    if answer != -1:
        return
    if start > end:
        return
    mid = (start+end)//2
    if current[mid] == mid:
        answer = mid
    elif current[mid] > mid:
        solution(current, start, mid-1)
    else:
        solution(current, mid+1, end)

N = int(input())
a_list = list(map(int, input().split()))
answer = -1
solution(a_list, 0, N-1)
print(answer)