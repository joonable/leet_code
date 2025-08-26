# TODO 헷갈림. 다시 풀어야 함.
def solution(H):
    stack = []
    blocks = 0
    for h in H:
        while stack and stack[-1] > h:
            stack.pop()
        if not stack or stack[-1] < h:
            stack.append(h)
            blocks += 1
        # else: stack[-1] == h → 연장, pass
    return blocks