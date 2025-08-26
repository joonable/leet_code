def solution(A):
    # Implement your solution here
    # [10,2,5,1,8,20] => (0,2,4)[10,5,8] =? 1
    # [1,2,5,8,10,20]
    # [10,50,5,1] => [1,5,10,50]

    A.sort()
    N = len(A)
    for i in range(2, N):
        x, y, z = A[i-2], A[i-1], A[i]
        if x + y > z and y + z > x and x + z > y:
            return 1
    return 0

def Solution_v2(A):
    A.sort()
    N = len(A)
    for i in range(2, N):
        x, y, z = A[i - 2], A[i - 1], A[i]
        if x + y > z:
            # 삼각형 조건은 사실상 x + y > z만 확인하면 충분
            # 나머지 두 조건(y+z>x, x+z>y)는 정렬 때문에 자동으로 참
            return 1
    return 0