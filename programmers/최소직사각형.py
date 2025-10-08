def solution(sizes):
    longs, shorts = [], []
    for w, h in sizes:
        if w > h:
            longs.append(w)
            shorts.append(h)
        else:
            longs.append(h)
            shorts.append(w)
    return max(longs) * max(shorts)