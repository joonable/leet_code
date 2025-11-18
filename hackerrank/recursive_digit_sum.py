def superDigit(n, k):
    super_digit = sum([int(ch) for ch in str(n)])
    if k != 1:
        super_digit *= k
    if super_digit < 10:
        return super_digit
    else:
        return superDigit(super_digit, 1)