from itertools import combinations

N, M = map(int, input().split())
city_map = [list(map(int, input().split())) for _ in range(N)]

chicken = []
house = []
for i in range(N):
    for j in range(N):
        if city_map[i][j] == 1:
            house.append([i, j])
        elif city_map[i][j] == 2:
            chicken.append([i, j])

store_value = [[0]*len(chicken) for _ in range(len(house))]
chicken_2 = []
for idx, hou in enumerate(house):
    for idx1, chic in enumerate(chicken):
        store_value[idx][idx1] = abs(hou[0]-chic[0]) + abs(hou[1]-chic[1])

for i in range(len(chicken)):
    chicken_2.append(i)


min_value = 999999
for i in range(1, M+1):
    for chic_list in combinations(chicken_2, i):
        chic_list = list(chic_list)
        temp_dis = 0
        for idx, hou in enumerate(house):
            dis = 999
            for chic_idx in chic_list:
                dis = min(dis, store_value[idx][chic_idx])
            temp_dis += dis
        min_value = min(min_value, temp_dis)
print(min_value)

