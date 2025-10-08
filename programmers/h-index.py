def solution(citations):
    citations.sort()
    n = len(citations)
    for i, citation in enumerate(citations):
        h_index = n - i
        if citation >= h_index:
            return h_index
    return 0