def solution(A):
    LIMIT = 1_000_000_000

    def merge_sort(arr):
        nonlocal inv_count
        n = len(arr)
        if n <= 1:
            return arr

        mid = n // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        merged = []
        i = j = 0

        # 병합하면서 inversion 계산
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                # left에 남아 있는 원소 수만큼 inversion 발생
                inv_count += len(left) - i
                if inv_count > LIMIT:
                    return []  # early stop
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    inv_count = 0
    merge_sort(A)

    return inv_count if inv_count <= LIMIT else -1