def solution(s):
    open_brackets = 0
    for ch in s:
        if ch == "(":
            open_brackets += 1
        else:
            if open_brackets <= 0:
                return False
            open_brackets -= 1
    return open_brackets == 0