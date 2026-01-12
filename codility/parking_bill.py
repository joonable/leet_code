# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(E, L):
    # Implement your solution here
    entered = [int(x) for x in E.split(":")]
    left = [int(x) for x in L.split(":")]

    m = left[1] - entered[1]
    h = left[0] - entered[0] + (1 if m > 0 else 0)

    return 5 + (h - 1) * 4
