def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    n_first = len(first)
    n_second = len(second)
    n_third = len(third)

    first_cnt = 0
    second_cnt = 0
    third_cnt = 0

    for i, answer in enumerate(answers):
        first_i = i % n_first
        if first[first_i] == answers[i]:
            first_cnt += 1

        second_i = i % n_second
        if second[second_i] == answers[i]:
            second_cnt += 1

        third_i = i % n_third
        if third[third_i] == answers[i]:
            third_cnt += 1

    answer = [1]
    if second_cnt > first_cnt:
        answer = [2]
    elif second_cnt == first_cnt:
        answer = [1, 2]
    else:
        pass

    if len(answer) == 1:
        if answer[0] == 1:
            if third_cnt > first_cnt:
                answer = [3]
            elif third_cnt == first_cnt:
                answer = [1, 3]
            else:
                pass
        else:
            if third_cnt > second_cnt:
                answer = [3]
            elif third_cnt == second_cnt:
                answer = [2, 3]
            else:
                pass
    else:
        if first_cnt == second_cnt == third_cnt:
            answer = [1, 2, 3]
        else:
            if first_cnt < third_cnt:
                answer = [3]
            else:
                pass
    return answer





