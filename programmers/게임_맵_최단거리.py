from collections import deque


def solution(maps):
    rows, cols = len(maps), len(maps[0])

    queue = deque([(0, 0)])
    answer = 0
    while queue:
        answer += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            maps[r][c] = 0
            if r == rows - 1 and c == cols - 1:
                return answer

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maps[nr][nc] == 1:
                    maps[nr][nc] = 0
                    queue.append((nr, nc))
    return -1

def solution_v2(maps):
    rows, cols = len(maps), len(maps[0])
    queue = deque([(0, 0)])

    while queue:
        r, c = queue.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maps[nr][nc] == 1:
                maps[nr][nc] = maps[r][c] + 1  # 이전 거리 + 1
                queue.append((nr, nc))

    return maps[rows - 1][cols - 1] if maps[rows - 1][cols - 1] > 1 else -1