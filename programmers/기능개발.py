# def solution(progresses, speeds):
#     days = []
#     for progress, speed in zip(progresses, speeds):
#         x, r = divmod(100 - progress, speed)
#         if r:
#             x += 1
#         if not days or days[-1] < x:
#             days.append(x)
#         else:
#             days.append(days[-1])
#
#     answer = [1]
#     for i in range(1, len(days)):
#         if days[i - 1] == days[i]:
#             answer[-1] += 1
#         else:
#             answer.append(1)
#     return answer


import math

def solution(progresses, speeds):
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]

    answer = []
    current = days[0]
    count = 1

    for d in days[1:]:
        if d <= current:  # 현재 배포일 이전(같은 배포 그룹)
            count += 1
        else:  # 새로운 배포 그룹 시작
            answer.append(count)
            current = d
            count = 1
    answer.append(count)
    return answer