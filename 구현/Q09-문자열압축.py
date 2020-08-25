def solution(s):
    answer = 0
    result_list = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)):
        result = ''
        length = len(s)//i
        cnt = 1
        for j in range(length):
            temp = s[i*j:i*(j+1)]
            temp_2 = s[i*(j+1):i*(j+2)]
            if temp == temp_2:
                cnt += 1
            elif temp != temp_2:
                if cnt > 1:
                    result += str(cnt) + temp
                    temp = temp_2
                    cnt = 1
                else:
                    result += temp
                    temp = temp_2
            if j == length-1:
                if cnt > 1:
                    result += str(cnt) + temp
                else:
                    result += temp_2
        result_list.append(len(result))
    answer = min(result_list)
    return answer
