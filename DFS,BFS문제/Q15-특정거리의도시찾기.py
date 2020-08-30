from collections import deque

N, M, K, X = map(int, input().split())
road_list = [[] for _ in range(N+1)]
visit_city = [0]*(N+1)
min_dis = [0]*(N+1)
result = []
for _ in range(M):
    a, b = map(int, input().split())
    road_list[a].append(b)
queue = deque([X])
visit_city[X] = 1
while queue:
    c_road = queue.popleft()
    if min_dis[c_road] == K:
        result.append(c_road)
    for next_road in road_list[c_road]:
        if visit_city[next_road] == 0:
            min_dis[next_road] = min_dis[c_road] + 1
            visit_city[next_road] = 1
            queue.append(next_road)

if result:
    result.sort()
    for l in range(len(result)):
        print(result[l])
else:
    print(-1)
