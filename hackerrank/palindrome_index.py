def palindromeIndex(s):
    def is_palindrome(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            if is_palindrome(left + 1, right):
                return left
            elif is_palindrome(left, right - 1):
                return right
            else:
                return -1
        left += 1
        right -= 1
    return -1
