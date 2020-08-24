# Q08-문자열 재정렬
S = list(input())
S.sort()
temp_list = []
for i in range(len(S)):
    if ord(S[i]) >= 65:
        temp_list = S[:i]
        S = S[i:]
        break
result = 0
for i in range(len(temp_list)):
    result += int(temp_list[i])
S.append(result)
print(''.join(map(str, S)))
