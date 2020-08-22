# Q03-문자열 뒤집기

S = list(input())
flag = '0'
count_zero = 0
count_one = 0
if S[0] == '0':
    count_zero = 1
else:
    count_one = 1
    flag = '1'
for num in S[1:]:
    if flag != num:
        flag = num
        if flag == '0':
            count_zero += 1
        elif flag == '1':
            count_one += 1
    else:
        continue
print(min(count_one, count_zero))