# Q07-럭키 스트레이트
N = list(map(int, input()))
result = 'READY'
left = N[:len(N)//2]
right = N[len(N)//2:]
if sum(left) == sum(right):
    result = 'LUCKY'
print(result)
