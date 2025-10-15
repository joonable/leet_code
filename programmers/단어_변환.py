from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    n = len(words)
    queue = deque([-1])
    visited = [False] * n

    answer = 0
    while queue:
        for _ in range(len(queue)):
            word_i = queue.popleft()
            word = words[word_i] if word_i != -1 else begin

            if word == target:
                return answer

            for i in range(n):
                if not visited[i]:
                    candidate = words[i]
                    diff = 0
                    for ch_w, ch_c in zip(word, candidate):
                        if ch_w != ch_c:
                            diff += 1
                            if diff > 1:
                                break

                    if diff == 1:
                        visited[i] = True
                        queue.append(i)
        answer += 1
    return 0


def solution_v2(begin, target, words):
    if target not in words:
        return 0

    n = len(words)
    visited = [False] * n
    queue = deque([(begin, 0)])  # (단어, 변환 횟수)

    while queue:
        word, steps = queue.popleft()
        if word == target:
            return steps

        for i in range(n):
            if not visited[i] and sum(a != b for a, b in zip(word, words[i])) == 1:
                visited[i] = True
                queue.append((words[i], steps + 1))

    return 0