# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution_dfs(A):
    if A == [[0]]:
        A = [[_ for _ in range(300_000)] for _ in range(300_000)]

    rows, cols = len(A), len(A[0])
    result = 0

    # [[0]] => 1
    # [[0], [0]] => 1
    # [[0, 0]] => 1
    # [[1, 2], [1, 2]] => 2
    # [[1, 1], [2, 2]] => 2
    # [[1, 2], [2, 1]] => 4

    def get_neighbours(r, c):
        return [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]

    def is_valid(r, c, colour):
        return 0 <= r < rows and 0 <= c < cols and A[r][c] == colour

    def dfs(r, c):
        colour = A[r][c]
        A[r][c] = None
        # print(colour)
        for nr, nc in get_neighbours(r, c):
            if is_valid(nr, nc, colour):
                dfs(nr, nc)

    for r in range(rows):
        for c in range(cols):
            if A[r][c] is not None:
                result += 1
                dfs(r, c)

    return result


from collections import deque


def solution_bfs(A):

    rows, cols = len(A), len(A[0])

    # [[0]] => 1
    # [[0], [0]] => 1
    # [[0, 0]] => 1
    # [[1, 2], [1, 2]] => 2
    # [[1, 1], [2, 2]] => 2
    # [[1, 2], [2, 1]] => 4

    DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

    result = 0
    for r in range(rows):
        for c in range(cols):
            if A[r][c] is None:
                continue
            result += 1
            queue = deque([(r, c)])
            colour = A[r][c]
            A[r][c] = None
            while queue:
                pr, pc = queue.popleft()
                for dr, dc in DIRS:
                    nr, nc = pr + dr, pc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and A[nr][nc] == colour:
                        A[nr][nc] = None
                        queue.append((nr, nc))
    return result


def solution(A):
    rows, cols = len(A), len(A[0])
    n = rows * cols
    visited = [False] * n
    grid = A  # 로컬 별칭

    res = 0
    for idx in range(n):
        if visited[idx]:
            continue
        res += 1
        color = grid[idx // cols][idx % cols]

        # 반복 DFS (스택)
        stack = [idx]
        visited[idx] = True

        while stack:
            cur = stack.pop()
            r = cur // cols
            c = cur % cols

            # 왼쪽
            if c > 0:
                nb = cur - 1
                if not visited[nb] and grid[r][c - 1] == color:
                    visited[nb] = True
                    stack.append(nb)

            # 오른쪽
            if c + 1 < cols:
                nb = cur + 1
                if not visited[nb] and grid[r][c + 1] == color:
                    visited[nb] = True
                    stack.append(nb)

            # 위
            if r > 0:
                nb = cur - cols
                if not visited[nb] and grid[r - 1][c] == color:
                    visited[nb] = True
                    stack.append(nb)

            # 아래
            if r + 1 < rows:
                nb = cur + cols
                if not visited[nb] and grid[r + 1][c] == color:
                    visited[nb] = True
                    stack.append(nb)

    return res