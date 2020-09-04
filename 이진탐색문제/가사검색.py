def binary_check(dir, query):
    start = 0
    end = len(query)-1
    while start <= end:
        mid = (start+end) // 2
        if dir == 0:  # 앞자리가 ? 인 경우
            if query[mid] != '?':
                end = mid - 1
            else:
                start = mid + 1
                index = mid
        else:
            if query[mid] != '?':
                start = mid + 1
            else:
                end = mid - 1
                index = mid
    return index


def find_start(length, words):
    result2, result = 0, 0
    for i in range(len(words)):
        if len(words[i]) == length:
            result2 = i
            break
    for j in range(len(words)-1, -1, -1):
        if len(words[j]) == length:
            result = j+1
            break
    return words[result2:result]


def solution(words, queries):
    answer = []
    words.sort(key=lambda x: len(x))
    for query in queries:
        length = len(query)
        if query[0] == '?':  # 앞자리가 ? 인 경우
            index = binary_check(0, query)
            temp = 0
            query_temp = query[index+1:]
        else:  # 뒷자리가 ?인 경우
            index = binary_check(1, query)
            temp = 1
            query_temp = query[:index]
        cnt = 0
        same_words = find_start(length, words)
        for word in same_words:

            if temp == 0:  # 앞자리가 ? 인 경우
                if word[index+1:] == query_temp:
                    cnt += 1
            elif temp == 1:  # 뒷자리가 ?인 경우
                if word[:index] == query_temp:
                    cnt += 1
        answer.append(cnt)

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))