T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
from collections import deque
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    l, r, t, b = 0, 1, 2, 3

    # pipes_in_out = {
    #     1: {l: [r], r: [l], t: [b], b: [t]},
    #     2: {l: [r], r: [l], t: [b], b: [t]},
    #     3: {l: [t, b], r: [t, b], t: [l, r], b: [l, r]},
    #     4: {l: [t, b], r: [t, b], t: [l, r], b: [l, r]},
    #     5: {l: [t, b], r: [t, b], t: [l, r], b: [l, r]},
    #     6: {l: [t, b], r: [t, b], t: [l, r], b: [l, r]}
    # }
    # pipe_curve = {l: [t, b], r: [t, b], t: [l, r], b: [l, r]}
    opposite_dir = {
        l: r, r: l, t: b, b: t
    }

    # pipe_type : { in_dir : out_dir }

    pipes_in_out = {
        # 1번 직선 (가로)
        1: {
            l: r,
            r: l,
        },

        # 2번 직선 (세로)
        2: {
            t: b,
            b: t,
        },

        # 3번 꺾인 파이프 (└ 모양)
        # left <-> top
        3: {
            l: t,
            t: l,
        },

        # 4번 꺾인 파이프 (┌ 모양)
        # top <-> right
        4: {
            t: r,
            r: t,
        },

        # 5번 꺾인 파이프 (┐ 모양)
        # right <-> bottom
        5: {
            r: b,
            b: r,
        },

        # 6번 꺾인 파이프 (┘ 모양)
        # bottom <-> left
        6: {
            b: l,
            l: b,
        },
    }
    visited = [[[False] * 4 for _ in range(N)] for _ in range(N)]
    # visited = [[[False] * 4 for _ in range(N)] for _ in range(N)]
    # visited = [[False] * N for _ in range(N)]
    out_dir_move = {l: (0, -1), r: (0, 1), t: (-1, 0), b: (1, 0)}
    answer = 0
    visited[0][0][l] = True
    queue = deque([((0, 0), l)])
    finished = False

    while queue and not finished:
        answer += 1
        for _ in range(len(queue)):
            (i, j), in_dir = queue.popleft()
            out_dirs = pipes_in_out[arr[i][j]][in_dir]
            if i == N - 1 and j == N - 1 and r in out_dirs:
                finished = True
                break
            for out_dir in out_dirs:
                move = out_dir_move[out_dir]
                ni, nj = (i + move[0], j + move[1])
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 0 \
                        and not visited[ni][nj][opposite_dir[out_dir]]:
                    visited[ni][nj][opposite_dir[out_dir]] = True

                    # and not visited[ni][nj][opposite_dir[out_dir]]:
                    # visited[ni][nj][opposite_dir[out_dir]] = True
                    queue.append(((ni, nj), opposite_dir[out_dir]))
    print(f"#{test_case} {answer}")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
from collections import deque

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    l, r, t, b = 0, 1, 2, 3

    # pipes_in_out = {
    #     1: {l: [r], r: [l], t: [b], b: [t]},
    #     2: {l: [r], r: [l], t: [b], b: [t]},
    #     3: {l: [t, b], r: [t, b], t: [l, r], b: [l, r]},
    #     4: {l: [t, b], r: [t, b], t: [l, r], b: [l, r]},
    #     5: {l: [t, b], r: [t, b], t: [l, r], b: [l, r]},
    #     6: {l: [t, b], r: [t, b], t: [l, r], b: [l, r]}
    # }
    # pipe_curve = {l: [t, b], r: [t, b], t: [l, r], b: [l, r]}
    opposite_dir = {
        l: r, r: l, t: b, b: t
    }

    # pipe_type : { in_dir : out_dir }

    pipes_in_out = {
        # 1번 직선 (가로)
        1: {
            l: r,
            r: l,
        },

        # 2번 직선 (세로)
        2: {
            t: b,
            b: t,
        },

        # 3번 꺾인 파이프 (└ 모양)
        # left <-> top
        3: {
            l: t,
            t: l,
        },

        # 4번 꺾인 파이프 (┌ 모양)
        # top <-> right
        4: {
            t: r,
            r: t,
        },

        # 5번 꺾인 파이프 (┐ 모양)
        # right <-> bottom
        5: {
            r: b,
            b: r,
        },

        # 6번 꺾인 파이프 (┘ 모양)
        # bottom <-> left
        6: {
            b: l,
            l: b,
        },
    }
    visited = [[[False] * 4 for _ in range(N)] for _ in range(N)]
    # visited = [[[False] * 4 for _ in range(N)] for _ in range(N)]
    # visited = [[False] * N for _ in range(N)]
    out_dir_move = {l: (0, -1), r: (0, 1), t: (-1, 0), b: (1, 0)}
    answer = 0
    visited[0][0][l] = True
    queue = deque([((0, 0), l)])
    finished = False

    while queue and not finished:
        answer += 1
        for _ in range(len(queue)):
            (i, j), in_dir = queue.popleft()

            # 이 방향으로 들어오는 게 가능한지
            out_dir = pipes_in_out[arr[i][j]].get(in_dir)
            if out_dir is None:
                continue

            # 종료 조건
            if i == N - 1 and j == N - 1 and out_dir == r:
                finished = True
                break

            move = out_dir_move[out_dir]
            ni, nj = i + move[0], j + move[1]

            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 0:
                next_in = opposite_dir[out_dir]
                if not visited[ni][nj][next_in]:
                    visited[ni][nj][next_in] = True
                    queue.append(((ni, nj), next_in))
    print(f"#{test_case} {answer}")

from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    l, r, t, b = 0, 1, 2, 3
    drdc = {
        l: (0, -1),
        r: (0, 1),
        t: (-1, 0),
        b: (1, 0),
    }
    opp = {l: r, r: l, t: b, b: t}

    # 가능한 "연결 포트 쌍" (회전까지 포함한 모든 가능한 형태)
    # 각 쌍은 (dir1, dir2)로 표현: 두 방향이 연결되어 있음.
    STRAIGHT_PAIRS = [(l, r), (t, b)]
    ELBOW_PAIRS = [(l, t), (t, r), (r, b), (b, l)]


    def get_pairs(pipe_type):
        if pipe_type == 0:
            return []
        if pipe_type in (1, 2):
            return STRAIGHT_PAIRS
        # 3,4,5,6
        return ELBOW_PAIRS


    # 이 칸(pipe_type)에 in_dir로 들어왔을 때 가능한 out_dir들 반환
    # (회전 선택에 의해 out이 여러 개일 수 있음)
    def possible_out_dirs(pipe_type, in_dir):
        outs = []
        for a, b_ in get_pairs(pipe_type):
            if in_dir == a:
                outs.append(b_)
            elif in_dir == b_:
                outs.append(a)
        return outs


    # 다음 칸이 next_in_dir(=반대방향)으로 "들어오는 것"이 가능한지 체크
    def can_accept(pipe_type, in_dir):
        if pipe_type == 0:
            return False
        for a, b_ in get_pairs(pipe_type):
            if in_dir == a or in_dir == b_:
                return True
        return False


    # visited[r][c][in_dir][out_dir]
    visited = [[[[False] * 4 for _ in range(4)] for _ in range(N)] for _ in range(N)]

    # 시작 조건: (0,0)은 왼쪽(in)에서 들어와야 함
    start_in = l
    found = False

    q = deque()
    # 시작점에서 가능한 out들
    for out_dir in possible_out_dirs(arr[0][0], start_in):
        visited[0][0][start_in][out_dir] = True
        q.append((0, 0, start_in, out_dir, 1))  # dist=1: 시작 파이프 포함 길이
    while q and not found:
        r0, c0, in_dir, out_dir, dist = q.popleft()

        # 현재 칸이 끝점이고, out이 반드시 오른쪽(r)이어야 성공
        if r0 == N - 1 and c0 == N - 1 and out_dir == r:
            found = True

        dr, dc = drdc[out_dir]
        nr, nc = r0 + dr, c0 + dc
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        if arr[nr][nc] == 0:
            continue

        next_in = opp[out_dir]
        # 이웃 파이프가 next_in으로 들어오는 걸 받아야 실제 연결 가능
        if not can_accept(arr[nr][nc], next_in):
            continue

        # 이웃 칸에서 next_in으로 들어왔을 때 가능한 out들을 확장
        for next_out in possible_out_dirs(arr[nr][nc], next_in):
            if not visited[nr][nc][next_in][next_out]:
                visited[nr][nc][next_in][next_out] = True
                q.append((nr, nc, next_in, next_out, dist + 1))

    print(f"#{tc} {dist}")

