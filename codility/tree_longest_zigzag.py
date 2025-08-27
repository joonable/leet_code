# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from extratypes import Tree  # library with types used in the task


def solution(T):
    def dfs(node, prev_direction):
        if not node:
            return 0
        if node.l:
            left = dfs(node.l, "l") + (0 if prev_direction == "l" else 1)
        else:
            left = 0

        if node.r:
            right = dfs(node.r, "r") + (1 if prev_direction == "l" else 0)
        else:
            right = 0
        # print(node.x, left, right)
        return max(left, right)

    return max(dfs(T.l, "l"), dfs(T.r, "r"))