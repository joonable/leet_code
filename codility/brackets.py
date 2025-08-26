# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # nested: empty, (U)[U]{U}, VW, VWU = nested_string,
    # {[()()]} => 1
    # ([)()] => 0
    # )( => 0
    # ()) => 0
    # (() => 0
    # [](){} => 1
    # [(){}] => 1
    # [({}){[]}] => 1

    if not S:
        return 1

    dict_brackets = {"}": "{", ")": "(", "]": "["}
    open_brackets = list(dict_brackets.values())

    stack = []
    for bracket in S:
        if bracket in open_brackets:
            stack.append(bracket)
        else:
            if not stack or dict_brackets[bracket] != stack.pop():
                return 0

    return 0 if stack else 1


