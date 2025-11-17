def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = set("0123456789")
    lower_case = set("abcdefghijklmnopqrstuvwxyz")
    upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    has_numbers, has_lower_case, has_upper_case, has_special_characters \
        = False, False, False, False
    for ch in password:
        if ch in numbers:
            has_numbers = True
        elif ch in lower_case:
            has_lower_case = True
        elif ch in upper_case:
            has_upper_case = True
        else:
            has_special_characters = True
    n_insert = 4 - (has_numbers + has_lower_case + has_upper_case + has_special_characters)
