
def solve(start, end, shops):
    n = len(shops)
    min_val = float("inf")
    def get_distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def backtrack(path, curr):
        nonlocal min_val
        # print(min_val)
        if not path:
            pass
        elif len(path) == 1:
            curr += get_distance(start, shops[path[-1]])
        else:
            curr += get_distance(shops[path[-2]], shops[path[-1]])
            if len(path) == n:
                curr += get_distance(shops[path[-1]], end)
                min_val = min(curr, min_val)

        if curr < min_val:
            for i in range(n):
                if i not in path:
                    path.append(i)
                    backtrack(path, curr)
                    path.pop()

    backtrack([], 0)
    return min_val


import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = [(arr[i], arr[i + 1]) for i in range(0, len(arr), 2)]
    answer = solve(arr[0], arr[1], arr[2:])
    print(f"#{test_case} {answer}")