from itertools import permutations


def cal_operate(x1, x2, cal):
    if cal == '+':
        answer = x1 + x2
    elif cal == '-':
        answer = x1 - x2
    elif cal == '*':
        answer = x1 * x2
    else:
        if x1 < 0:
            answer = -(abs(x1)//x2)
        else:
            answer = x1 // x2
    return answer


N = int(input())
cal_list = list(map(int, input().split()))
operator_list = list(map(int, input().split()))  # ('+', '-', '*', '/') 연산자 순서

operator = operator_list[0]*'+'+operator_list[1]*'-'+operator_list[2]*'*'+operator_list[3]*'/'
operator = list(operator)

result = []
calculator = list(set(permutations(operator, N-1)))
for i in range(len(calculator)):
    cal_sum = cal_list[0]
    for j in range(1, N):
        cal_sum = cal_operate(cal_sum, cal_list[j], calculator[i][j-1])
    if cal_sum not in result:
        result.append(cal_sum)
print(max(result))
print(min(result))