def largestRectangle(h):
    stack = []
    h.append(0)
    max_area = -1
    for r, r_height in enumerate(h):
        while stack and h[stack[-1]] > r_height:
            l = stack.pop()
            height = h[l]
            width = r if not stack else r - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(r)
    return max_area