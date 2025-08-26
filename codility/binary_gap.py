def solution(N):
    result = 0
    curr_len = 0
    found_one = False

    while N > 0:
        N, r = divmod(N, 2)
        if r == 1:
            found_one = True
            result = max(result, curr_len)
            curr_len = 0
        else:
            if found_one:
                curr_len += 1
    return result

def solution_v2(N):
    # 1) 뒤쪽(LSB)부터 이어지는 0들 제거: 마지막 1 뒤의 0은 갭이 아님
    while N > 0 and (N & 1) == 0:
        N >>= 1

    longest = 0
    curr = 0
    while N > 0:
        if N & 1:           # 비트가 1
            if curr > longest:
                longest = curr
            curr = 0
        else:               # 비트가 0
            curr += 1
        N >>= 1
    return longest

def solution_v3(N):
    b = bin(N)[2:].strip('0')
    return max((len(z) for z in b.split('1')), default=0)