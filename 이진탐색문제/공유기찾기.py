N, C = map(int, input().split())
house = []
for _ in range(N):
    house.append(int(input()))
house.sort()

start = house[1] - house[0]  # 가장 짧은 거리
end = house[-1] - house[0]  # 가장 긴 거리

while start <= end:
    mid = (start + end) // 2  # 중간 거리
    value = house[0]
    cnt = 1
    for i in range(1, N):
        if house[i] >= value + mid:
            cnt += 1
            value = house[i]

    if C > cnt:   # 공유기를 설치를 다 못한 경우
        end = mid - 1

    elif C <= cnt:
        result = mid
        start = mid + 1
print(result)