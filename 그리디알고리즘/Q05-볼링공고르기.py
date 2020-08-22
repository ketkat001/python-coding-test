# Q05. 볼링공 고르기

N, M = map(int, input().split())
balling = list(map(int, input().split()))
balling.sort()
result = N*(N-1)//2
weight = 0
temp = 1
for ball in balling:
    if weight != ball:
        weight = ball
        result -= temp*(temp-1)//2
        temp = 1
    else:
        temp += 1
result -= temp*(temp-1)//2

print(result)