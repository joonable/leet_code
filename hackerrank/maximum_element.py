def getMax(operations):
    stack = []
    max_stack = [0]
    result = []
    for op in operations:
        if op.startswith("1 "):
            _, num = op.split(" ")
            num = int(num)
            max_num = max(num, max_stack[-1])
            stack.append(num)
            max_stack.append(max_num)
        else:
            if op == "2":
                stack.pop()
                max_stack.pop()
            else:
                result.append(str(max_stack[-1]))
    return result