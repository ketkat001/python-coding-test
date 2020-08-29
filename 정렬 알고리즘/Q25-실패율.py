def solution(N, stages):
    stages.sort(reverse=True)
    current_stage = stages[0]
    all_cnt = 1
    cnt = 1
    failure_list = [[i, 0] for i in range(N+2)]
    for stage in stages[1:]:
        if stage == current_stage:
            cnt += 1
            all_cnt += 1
            failure_list[current_stage][1] = cnt / all_cnt
        else:
            failure_list[current_stage][1] = cnt / all_cnt
            cnt = 1
            all_cnt += 1
            current_stage = stage
    result = sorted(failure_list[1:N+1], key=lambda x:(-x[1], x[0]))
    answer = []
    for p in range(len(result)):
        answer.append(result[p][0])
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
