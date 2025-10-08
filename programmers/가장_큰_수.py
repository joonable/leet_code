def solution(numbers):
    numbers = list(map(str, numbers))

    numbers.sort(key=lambda x: x*4, reverse=True)

    result = ''.join(numbers)
    result = '0' if result[0] == '0' else result
    return result