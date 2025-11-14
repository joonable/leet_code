from functools import cmp_to_key
def bigSorting(unsorted):
    def compare(x, y):
        if len(x) > len(y):
            return 1
        elif len(x) < len(y):
            return -1
        elif x > y:
            return 1
        elif x < y:
            return -1
        else:
            return 0
    return sorted(unsorted, key=cmp_to_key(compare))