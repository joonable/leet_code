from math import gcd, lcm
def getTotalX(a, b):
    lcm_a = lcm(*a)
    gcd_b = gcd(*b)
    result = 0
    for i in range(lcm_a, gcd_b + 1, lcm_a):
        if gcd_b % i == 0:
            result += 1
    return result