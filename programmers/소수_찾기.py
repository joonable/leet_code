from itertools import permutations

def solution(numbers):
    candidates = []
    for i in range(1, len(numbers) + 1):
        candidates.extend([int("".join(tup)) for tup in permutations(numbers, i)])
    candidates = list(set(candidates))

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    answer = 0
    for candidate in candidates:
        if is_prime(candidate):
            answer += 1

    return answer