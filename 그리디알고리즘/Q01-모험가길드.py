# 그리드 알고리즘 - 모험가 길드

N = int(input())
traveler = list(map(int, input().split()))
traveler.sort()
team = 0             # 한 팀에 몇명
result = 0           # 총 몇팀
for fear in traveler:
    team += 1
    if team >= fear:
        result += 1
        team = 0
print(result)