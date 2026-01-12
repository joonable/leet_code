T = int(input())
from collections import deque
def solve(arr, N, M, pos, n_iter):
    L, U, R, D = (0, -1), (-1, 0), (0, 1), (1, 0)
    opposite = {
        L: R,
        R: L,
        U: D,
        D: U
    }
    pipe_move = [
        [],
        {L, U, R, D},
        {U, D},
        {L, R},
        {U, R},
        {R, D},
        {D, L},
        {L, U}
    ]

    queue = deque([pos])
    visited = [[False] * M for _ in range(N)]
    visited[pos[0]][pos[1]] = True

    cnt = 0
    for _ in range(n_iter):
        cnt += len(queue)
        for _ in range(len(queue)):
            r, c = queue.popleft()
            moves = pipe_move[arr[r][c]]
            for move in moves:
                nr, nc = r + move[0], c + move[1]
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] \
                        and (opposite[move] in pipe_move[arr[nr][nc]]):
                    visited[nr][nc] = True
                    queue.append((nr, nc))
    return cnt

for test_case in range(1, T + 1):
    N, M, R, C, L = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = solve(arr, N, M, (R, C), L)
    print(f"#{test_case} {answer}")