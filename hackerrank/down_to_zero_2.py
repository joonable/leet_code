#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'downToZero' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.

from math import sqrt
from collections import deque


def downToZero(n):
    visited = [False] * (n + 1)
    queue = deque([(n, 0)])

    visited[n] = True
    while queue:
        val, steps = queue.popleft()
        if not val:
            return steps

        if not visited[val - 1]:
            visited[val - 1] = True
            queue.append((val - 1, steps + 1))

        for i in range(2, int(sqrt(val)) + 1):
            if val % i == 0:
                nxt = max(i, val // i)
                if not visited[nxt]:
                    visited[nxt] = True
                    queue.append((nxt, steps + 1))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = downToZero(n)

        fptr.write(str(result) + '\n')

    fptr.close()
