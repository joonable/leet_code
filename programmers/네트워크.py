class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            return True
        return False


def solution_uf(n, computers):
    uf = UnionFind(n)

    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                uf.union(i, j)

    for i in range(n):
        uf.find(i)

    return len(set(uf.parent))


def solution_dfs(n, computers):
    visited = [False] * n

    def dfs(node):
        visited[node] = True
        for nxt in range(n):
            if not visited[nxt] and computers[node][nxt] == 1:
                dfs(nxt)

    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1

    return count

