#Q04-만들 수 없는 금액

N = int(input())
money = list(map(int, input().split()))
money.sort()
result = 1
for m in money:
    if m > result:
        break
    result += m
print(result)