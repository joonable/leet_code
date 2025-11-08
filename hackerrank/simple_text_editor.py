class TextEditor():
    def __init__(self):
        self.s = []
        self.history = []

    def append(self, s):
        self.history.append(self.s[:])
        self.s.extend(list(s))

    def delete(self, k):
        self.history.append(self.s[:])
        self.s = self.s[:-int(k)]

    def print_k(self, k):
        print(self.s[int(k) - 1])

    def undo(self):
        self.s = self.history.pop()


Q = int(input())
te = TextEditor()
for _ in range(Q):
    ops = input().split()
    if len(ops) == 1:
        te.undo()
        continue

    op, arg = ops[0], ops[1]
    if op == "1":
        te.append(arg)
    elif op == "2":
        te.delete(arg)
    elif op == "3":
        te.print_k(arg)
