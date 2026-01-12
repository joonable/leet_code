def solution(A, B):
    # Implement your solution here
    result = []
    while A or B:
        if A > B:
            result.append("a" * min(2, A))
            result.append("b" * min(1, B))
            A -= min(2, A)
            B -= min(1, B)
        elif A < B:
            result.append("b" * min(2, B))
            result.append("a" * min(1, A))
            B -= min(2, B)
            A -= min(1, A)
        else:
            if not result or result[-1] == "b":
                result.append("ab" * ((A + B) // 2))
            else:
                result.append("ba" * ((A + B) // 2))
            A = 0
            B = 0

    return "".join(result)