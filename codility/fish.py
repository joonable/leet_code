def solution(A, B):
    # Implement your solution here
    # N = len(A) = len(B)
    # A[i], B[i]: fish
    # P < Q: P is initially upstream of fish Q
    # A[P]: unique sizes, B[P]: direction (0: up, 1: down)
    # whem they meet, the larger fish eats the smaller one
    # result: the number of fish that will stay alive

    # ([4,3,2,1,5], [0,1,0,0,0]) => 2
    # ([4,3,2,1,5], [0,1,1,0,0]) => 2
    # ([4,3,2], [0,0,0]) => 3
    # ([4,3,2], [1,1,1]) => 3
    # ([4,3,2], [1,0,1]) => 2
    # ([2,3,4], [1,0,1]) => 2

    one_fish = []
    alive_zero_fish = 0
    for size, direction in zip(A, B):
        if one_fish and direction == 0:
            while one_fish and one_fish[-1] < size:
                one_fish.pop()
            if not one_fish:
                alive_zero_fish += 1
        else:
            if direction == 1:
                one_fish.append(size)
            else:
                alive_zero_fish += 1
    return alive_zero_fish + len(one_fish)


def solution(A, B):
    down = []            # 하류(1) 물고기 크기 스택
    alive_up = 0
    for size, dir in zip(A, B):
        if dir == 1:     # 하류면 스택에 쌓기
            down.append(size)
            continue
        # 상류면 스택의 하류들과 싸움
        while down and down[-1] < size:
            down.pop()
        if not down:     # 모두 물리쳤다면 상류 생존
            alive_up += 1
        # else: 더 큰 하류가 있어 상류 탈락
    return alive_up + len(down)