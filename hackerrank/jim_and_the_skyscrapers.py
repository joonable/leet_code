def solve(arr):
    stack = []
    arr.append(float("inf"))
    result = 0

    for h in arr:
        cnt = 1
        while stack and stack[-1] < h:
            prev_h = stack.pop()
            if stack and prev_h == stack[-1]:
                cnt += 1
            else:
                result += (cnt - 1) * cnt
                cnt = 1
        stack.append(h)
    return result