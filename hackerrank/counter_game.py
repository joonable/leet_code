def counterGame(n):
    # Write your code here
    def get_lower_power_2(x):
        if x % 2 == 0:
            return x // 2
        else:
            i = 1
            while not 2 ** i <= x < 2 ** (i + 1):
                i += 1
            return x - 2 ** i

    is_louise = False
    while n != 1:
        n = get_lower_power_2(n)
        is_louise = not is_louise
    return "Louise" if is_louise else "Richard"