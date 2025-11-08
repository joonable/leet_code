class Trie():
    def __init__(self):
        self.children = {}
        self.count = 0

    def add(self, name):
        trie = self
        trie.count += 1
        for ch in name:
            if ch not in trie.children:
                trie.children[ch] = Trie()
            trie = trie.children[ch]
            trie.count += 1

    def find(self, partial):
        trie = self
        for ch in partial:
            if ch not in trie.children:
                return 0
            trie = trie.children[ch]
        return trie.count


def contacts(queries):
    contacts = Trie()
    result = []
    for op, s in queries:
        if op == "add":
            contacts.add(s)
        else:
            result.append(contacts.find(s))
    return result