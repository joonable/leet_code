def solution(n, lost, reserve):
    clothes = [0] + [1 for _ in range(n)] + [0]
    for i in lost:
        clothes[i] = 0
    for i in reserve:
        clothes[i] += 1

    answer = 0
    for i in range(1, n + 1):
        c = clothes[i]
        if c == 0:
            if clothes[i - 1] == 1:
                clothes[i - 1] -= 1
                answer += 1
            elif clothes[i + 1] == 2:
                clothes[i + 1] -= 1
                answer += 1
        else:
            clothes[i] -= 1
            answer += 1

    return answer