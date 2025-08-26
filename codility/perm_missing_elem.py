def solution(A):
    # Implement your solution here
    # A in [1..(N + 1)]
    # N = len(A) [0~100,000]
    # [2,3,1,5] => 4
    # [] => 1
    # [1] => 2
    # [2] => 1

    N = len(A)
    set_elems = set(range(1, N + 2))
    for num in A:
        set_elems.remove(num)
    return set_elems.pop()

def solution_sum(A):
    N = len(A)
    total = (N + 1) * (N + 2) // 2
    return total - sum(A)

def solution_xor(A):
    N = len(A)
    result = 0
    for i in range(1, N+2):   # 1 ~ N+1
        result ^= i
    for num in A:
        result ^= num
    return result