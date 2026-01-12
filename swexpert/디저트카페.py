T = int(input())

def solve(arr, N):
    answer = -1

    DIRS = [
        (1, 1),
        (1, -1),
        (-1, -1),
        (-1, 1),
    ]
    for r in range(N):
        for c in range(N):
            max_a = min(N - 1 - r, N - 1 - c)
            for a in range(1, max_a + 1):
                max_b = min(N - 1 - r - a, c)
                for b in range(1, max_b + 1):

                    desserts = set()
                    cr, cc = r, c
                    desserts.add(arr[cr][cc])
                    valid = True
                    cnt = 1

                    for d, steps in enumerate([a, b, a, b]):
                        dr, dc = DIRS[d]
                        for _ in range(steps):
                            cr += dr
                            cc += dc

                            if cr == r and cc == c:
                                break

                            if arr[cr][cc] in desserts:
                                valid = False
                                break

                            desserts.add(arr[cr][cc])
                            cnt += 1

                        if not valid:
                            break

                    if valid and cr == r and cc == c:
                        answer = max(answer, cnt)

    return answer


for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = solve(arr, n)

    print(f"#{test_case} {answer}")