# Q02- 곱하기 혹은 더하기

S = list(input())
result = 0
for num in S:
    if result == 0 or num == '0':
        result += int(num)
    else:
        result *= int(num)
print(result)