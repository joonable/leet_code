# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import Counter


def solution(A):
    # leader: value that occurs in more than half of the elements of A
    # equi leader: index S, such that leader(A[:S+1]), leader([S+1:]) 0 ≤ S < N - 1)
    # count the number of equi leaders
    # [4,3,4,4,4,2] => 0, 2 => 2

    # [4,4,4] => 2
    # [4,4] => 1
    # [0] => 0
    # [4,1,1,4] => 0
    # [1,2,3] => 0

    # [1,1,2] => 0
    # [1,1,2,2] => 0
    # [1,2,1,1,2,1] => 3
    # [1,2] => 0
    # [9,9,10,9] => 2

    front_counter = Counter()
    back_counter = Counter(A)
    eq_count = 0
    N = len(A)
    prev_leader = A[0]
    for i, num in enumerate(A):
        front_counter[num] += 1
        back_counter[num] -= 1
        # print()
        # print(f"{front_counter[num]} > {(i + 1) / 2}")
        # print(f"{back_counter[num]} > {(N - i - 1) / 2}")
        if front_counter[num] > (i + 1) / 2 \
                and back_counter[num] > (N - i - 1) / 2:
            # print(i)
            eq_count += 1
            prev_leader = num
        elif front_counter[prev_leader] > (i + 1) / 2 \
                and back_counter[prev_leader] > (N - i - 1) / 2:
            # print(i)
            eq_count += 1
        # print(N, i + 1, N - i - 1)
    return eq_count