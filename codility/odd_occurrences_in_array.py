from collections import defaultdict

def solution(A):
    # A non-empty array A
    # N = len(A) such that N % 2 => 1

    # [9, 3, 9, 3, 9, 7, 9] => 7
    # [9, 9, 9, 9, 9, 9, 9] => 9
    # [9] => 9
    # [1000000000] => 1000000000

    dict_visited = defaultdict(bool)
    for num in A:
        if dict_visited[num]:
            del dict_visited[num]
        else:
            dict_visited[num] = True
    return list(dict_visited.keys())[0]


def solution_xor(A):
    """
    XOR(^)의 성질:
	1.	a ^ a = 0 (같은 수를 두 번 XOR하면 사라짐)
	2.	a ^ 0 = a (0은 항등원 역할)
	3.	순서와 묶음은 상관없음 (교환법칙, 결합법칙 성립)
    따라서 배열 전체를 XOR하면 짝수 번 나온 수는 다 사라지고, 홀수 번 나온 수만 남음.

    """
    result = 0
    for num in A:
        result ^= num   # 같은 숫자는 서로 소거됨
    return result