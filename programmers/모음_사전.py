from itertools import product


def solution(word):
    list_products = []
    for i in range(1, 6):
        list_products.extend(product(['A', 'E', 'I', 'O', 'U'], repeat=i))
    list_products = sorted(
        ["".join(list(_product)) for _product in list_products]
    )
    for i in range(len(list_products)):
        if word == list_products[i]:
            return i + 1
