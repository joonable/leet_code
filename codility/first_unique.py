# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import Counter


def solution(A):
    # Implement your solution here
    counter = Counter(A)
    for a in A:
        if counter[a] == 1:
            return a
    return -1


